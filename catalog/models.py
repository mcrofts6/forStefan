from django.db import models
from mysite import settings
from decimal import Decimal

TAX_RATE = Decimal("0.05")


class Category(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    name = models.TextField(null=False)


class Product(models.Model):
    product_status = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=False
    )
    last_modified = models.DateTimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=product_status, default='A', null=False)
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    quantity=models.IntegerField(default=2, null=False)
    reorder_trigger=models.IntegerField(default=0, null=False)
    reorder_quantity=models.IntegerField(default=5, null=False)

    def image_url(self):
        pimage = ProductImage.objects.filter(product = self.id).first()
        if pimage is None:
            return settings.STATIC_URL + "catalog/media/products/media/products/" + "notfound.jpg"
        return settings.STATIC_URL + "catalog/media/products/media/products/" + pimage.filename

    def images_url(self):
        images_url=[]
        return images_url

    def images_urls(self):
        pimages = ProductImage.objects.filter(product=self)
        image_urls=[]

        for p in pimages:
            image_urls.append(p.image_url())

        if image_urls.count == 0:
            image_urls[0] = settings.STATIC_URL + "catalog/media/products/media/products/notfound.jpg"
        return image_urls

class ProductImage(models.Model):
    filename = models.TextField()
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        null=False
    )
    last_modified = models.DateTimeField(auto_now=True)

    def image_url(self):
        self.url = "notfound.jpg"
        if self.filename is not None:
            self.url = settings.STATIC_URL + "catalog/media/products/media/products/" + self.filename
        return self.url

class Sale(models.Model):
    user = models.ForeignKey("account.User", on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    purchased = models.DateTimeField(null=True, default=None)
    subtotal = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    tax = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    total = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    charge_id = models.TextField(null=True, default=None)   # successful charge id from stripe

    def recalculate(self):
        subtotal = 0
        total = 0

        for i in SaleItem.objects.filter(sale=self, status='A'):
            subtotal = subtotal + (i.price * i.quantity)
            tax = subtotal * TAX_RATE
            total = tax + subtotal
        return subtotal, tax, total

    def finalize(self, stripeToken):
        if self.purchased is not None 
            raise ValueError("This sale has already been finalized")

        for i in SaleItem.objects.filter(sale=self):
            if i.quantity > i.product.quantity
                raise ValueError("There is not enough inventory to complete the order.")
            
        self.recalculate()
        charge = stripe.Charge.create(
            amount=self.total * Decimal('100.0'),
            currency='usd',
            description='Testing charge',
            source=stripeToken,
        )
        self.charge_id = settings.STRIPE_SECRET_KEY
        self.purchased = now
        self.save()

class SaleItem(models.Model):
    STATUS_CHOICES = [
        ( 'A', 'Active' ),
        ( 'D', 'Deleted' ),
    ]
    status = models.CharField(max_length=1, default=STATUS_CHOICES[0][0], choices=STATUS_CHOICES)
    sale = models.ForeignKey("Sale", on_delete=models.PROTECT, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal(0))
    class Meta:
        ordering = [ 'product__name' ]
