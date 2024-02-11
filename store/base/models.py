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
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0)
    reviews = models.IntegerField(default=0)
    sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Address(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    address = models.TextField()
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.contact_name}'s Address"
    
class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        # Add more status choices as needed
    )
        
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Order for {self.user.username} - {self.product.name}"
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    review = models.CharField(max_length=500)

    def __str__(self):
        return f"Review for product {self.product}"
