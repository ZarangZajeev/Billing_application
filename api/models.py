from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class USerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    shop_name=models.CharField(max_length=200)
    phone=models.PositiveIntegerField()
    logo=models.ImageField(upload_to='logos',default='images/logo.png',null=True)

    def __str__(self):
        return self.shop_name
    
class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,related_name="product-category",on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    user=models.ForeignKey(User,related_name="product-user",on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    create_at=models.DateTimeField(auto_now_add=True)
    qty=models.PositiveIntegerField()
    product_img=models.ImageField(upload_to='products_img',default='images/product.png',null=True)

    def __str__(self):
        return self.name
    
class Bill(models.Model):
    product=models.ForeignKey(Products,related_name="bill-product",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    quantity=models.PositiveIntegerField()
    user=models.ForeignKey(User,related_name="bill-user")
    customer_name=models.CharField(max_length=200)
    customer_phone=models.PositiveBigIntegerField()
    total_amount=models.PositiveIntegerField()