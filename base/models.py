from django.db import models

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