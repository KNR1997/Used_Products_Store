from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('seller', 'Seller'),
        ('admin', 'Admin'),
        # Add more roles as needed
    )

    # Add your custom fields here
    # For example, you might add fields like profile_picture, address, etc.
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    # Add any other custom fields as needed

    def __str__(self):
        return self.username
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name