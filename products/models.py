from django.db import models
from django.contrib.auth.models import User
from django.utils.text import timezone 

FLAG_Types = (
    ('Sale','Sale'),
    ('New','New'),
    ('Feature','Feature'),
)

class Product(models.Model):
    name = models.CharField(max_length=120)
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=100000)
    image = models.ImageField(upload_to='products')
    price = models.FloatField()
    flag = models.CharField(max_length=10,choices=FLAG_Types)
    brand = models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    sku = models.CharField(max_length=12)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='brands')

    def __str__(self):
        return self.name
    

class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    product = models.ForeignKey(Product,related_name='product_review',on_delete=models.CASCADE)
    rate = models.IntegerField()
    feedback = models.TextField(max_length=400)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.user)