from django.db import models
from user.models import User
from main.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.email
