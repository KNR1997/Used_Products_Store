from typing import Any
from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser, PermissionManager, AbstractBaseUser
from django.utils import timezone

# Create your models here.
class book(models.Model):
    title = models.CharField(max_length = 45)
    author = models.CharField(max_length = 45)
    description = models.TextField()
    copies = models.IntegerField()
    copies_available = models.IntegerField()
    category = models.CharField(max_length = 45)
    img = models.BinaryField()

class checkout(models.Model):
    user_email = models.CharField(max_length = 45)
    checkout_date = models.CharField(max_length = 45)
    return_date = models.TextField()
    book_id = models.BigIntegerField()

class history(models.Model):
    user_email = models.CharField(max_length = 45)
    checkout_date = models.CharField(max_length = 45)
    returned_date = models.TextField()
    title = models.IntegerField()
    author = models.IntegerField()
    description = models.CharField(max_length = 45)
    img = models.BinaryField()

class messages(models.Model):
    user_email = models.CharField(max_length = 45)
    title = models.CharField(max_length = 45)
    question = models.TextField()
    admin_email = models.CharField(max_length = 45)
    response = models.TextField()
    closed = models.SmallIntegerField()

class review(models.Model):
    user_email = models.CharField(max_length = 45)
    date = models.DateTimeField()
    rating = models.DecimalField(max_digits = 3, decimal_places = 2)
    book_id = models.BigIntegerField()
    review_description = models.TextField()
    
class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        SELLER = 'SELLER', 'Seller'
        BUYER = 'BUYER', 'Buyer'

    base_role = Role.ADMIN

    role = models.CharField(max_length=50, choices=Role.choices)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)
    
    
# class CustomUserManager(UserManager):
#     def _create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError("Please provide a email")
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)

#         return user
    
#     def create_user(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', False)
#         extra_fields.setdefault('is_superuser', False)
#         return self._create_user(email, password, **extra_fields)
    
#     def create_superuser(self, email=None, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self._create_user(email, password, **extra_fields)
    
# class User(AbstractBaseUser, PermissionManager):
#     email = models.EmailField(blank=True, default='', unique=True)
#     name = models.CharField(max_length=255, blank=True, default='')

#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)

#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(blank=True, null=True)

#     objects = CustomUserManager()

#     USERNAME_FIELD = 'email'
#     EMAIL_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     class Meta:
#         verbose_name = 'User'
#         verbose_name_plural = 'Users'

#     def get_full_name(self):
#         return self.name
    
#     def get_short_name(self):
#         return self.name or self.email.split('@')[0]