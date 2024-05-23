from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email,
        first name, second name and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email)
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, first name, 
        second name and password.
        """

        email = self.normalize_email(email)
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=128, null=False)
    second_name = models.CharField(max_length=128, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    link = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=200, null=False)

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
