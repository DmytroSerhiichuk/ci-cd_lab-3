from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    link = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200, null=False)
    link = models.CharField(max_length=200, null=False, unique=True, blank=True, default='')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=False, default=0)

    def save(self, *args, **kwargs):
        if self.link == '':
            self.link = self.name.lower().strip().replace(' ', '-')
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
