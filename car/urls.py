from django.urls import path
from .import views

urlpatterns = [

    path("CarAdd",views.CarAdd,name="CarAdd"),
    path("ViewCarlist",views.ViewCarlist,name="ViewCarlist"),
    path("UpdateCar/<int:pk>",views.UpdateCar,name="UpdateCar"),
    path("DeleteCar/<int:pk>",views.DeleteCar,name="DeleteCar"),
    path("ViewCar/<int:pk>",views.ViewCar,name="ViewCar"),
    path("ViewAll",views.ViewAll,name="ViewAll"),
    path("ViewOrder",views.ViewOrder,name="ViewOrder"),
    path("IdProof/<int:pk>",views.IdProof,name="IdProof"),
   





]