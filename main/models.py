from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=False, unique=True)
    link = models.CharField(max_length=200, null=False, unique=True, blank=True, default='')
    image = models.ImageField(upload_to='category_images', null=True)

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
    name = models.CharField(max_length=200, null=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, default=0)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, null=False, default=0)
    price = models.PositiveIntegerField(null=False, default=1)
    image = models.ImageField(upload_to='product_images', null=True)
    description = models.CharField(max_length=2000, null=False, default='Lorem ipsum')

    def __str__(self):
        return self.name
