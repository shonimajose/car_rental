from django.db import models
from django.contrib.auth.models import User

class CarDetail(models.Model):

    
    CarId = models.AutoField(primary_key=True)
    Car_Name=models.CharField(max_length=255)
    Car_Brand=models.CharField(max_length=255)
    Car_Discription=models.CharField(max_length=1000)
    Car_Rent=models.IntegerField()
    Car_Image=models.ImageField(upload_to="car_image")
    Owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)





# Create your models here.
