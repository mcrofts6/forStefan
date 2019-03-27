from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthdate = models.DateTimeField(null=True)
    favcolor = models.TextField(null=True)
       
    def get_shopping_cart(self):
        from catalog import models as cmod

        sale = cmod.Sale.objects.filter(user=self, purchased=None).first() 
        if sale is None
            sale = cmod.Sale.objects.create(user=self)
        return(sale)


