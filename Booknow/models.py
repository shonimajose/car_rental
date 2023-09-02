from django.db import models
from car.models import CarDetail
from django.contrib.auth.models import User

class Book(models.Model):
    car = models.ForeignKey(CarDetail,on_delete=models.CASCADE ,null=True,blank=True)
    numberofdays = models.IntegerField()
    Booker_Name =models.CharField(max_length=255)
    Address=models.CharField(max_length=1000)
    Id_Proof=models.ImageField(upload_to="id_image")
    user = models.ForeignKey(User,on_delete=models.CASCADE ,null=True,blank=True)
    status = models.BooleanField(default=False)


class BookedCar(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE ,)
    TotalRent = models.IntegerField()
    paymentstatus = models.BooleanField(default=False)
    cancel = models.BooleanField(default=False)

    

# Create your models here.
