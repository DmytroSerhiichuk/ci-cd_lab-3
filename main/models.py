from django.db import models
from user.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    
    link = models.CharField(max_length=200, null=False, unique=True, blank=True, default='')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.link == '':
            self.link = self.name.lower().strip().replace(' ', '-')
        super(Category, self).save(*args, **kwargs)
    
class Brand(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    price = models.FloatField(default=0.00)
    name = models.CharField(max_length=200, null=False)
    link = models.CharField(max_length=200, null=False, unique=True, blank=True, default='')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, default=0)
    image = models.ImageField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.link == '':
            self.link = self.name.lower().strip().replace(' ', '-')
        super(Product, self).save(*args, **kwargs)

    def showImage(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    date = models.DateTimeField(null=True, blank=False)


    def __str__(self):
        return str(self.id)
    
    def getCartTotal(self):
        orderitems = self.purchaseitem_set.all()
        total = sum([item.getTotal() for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def getTotal(self):
        total = self.movie.price * self.quantity
        return total