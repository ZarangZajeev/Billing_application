from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class USerProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    shop_name=models.CharField(max_length=200)
    phone=models.PositiveIntegerField()
    logo=models.ImageField(upload_to='logos',default='default.png')

    def __str__(self):
        return self.shop_name