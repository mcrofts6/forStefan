from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    last_modified = models.DatetimeField(auto_now=True)
    name = models.TextField(null=False)

class Product(model.Model):
    STATUS_CHOICES = (
        ('A','Active'),
        ('I', 'Inactive'),
    )
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False)
    last_modified = models.DatetimeField(auto_now=True)
    status = models.TextField(db_index=True, choices=STATUS_CHOICES, default='A', null=False)
    name = models.TextField(null=False)
    description = models.TextField(null=False)
    price = models.DecimalField(max_digits=(6), decimal_places=2, null=False)
    quantity = models.IntegerField(default=0, null=False)
    reorder_trigger = models.IntegerField(default=2, null=False)
    reorder_quantity = models.IntegerField(default=5, null=False)

    def image_url(self):
        return self.images_url()[0]

    def images_url(self):
        pimages = ProductImage.objects.filter(product=self)
        urls = []
        for p in pimages:
            urls.append(p.image_url())  #referencing ProductImage
        if urls.count == 0:
            urls[0] = settings.STATIC_URL + "catalog/media/products/notfound.jpg"
        return urls

class ProductImage(models.Model):
    last_modified = models.DateTimeField(auto_now=True)
    filename = models.TextField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')

    def image_url(self):
    return settings.STATIC_URL + "cataog/media/products/" + self.filename