from django.urls import path
from .import views

urlpatterns = [
    path("BookNow/<int:pk>",views.BookNow,name="BookNow"),
    path("Order/<int:pk>",views.Order,name="Order"),
    path("Placeorder/<int:pk>",views.Placeorder,name="Placeorder"),
    path("Booking",views.Booking,name="Booking"),
    path("cancel/<int:pk>",views.cancel,name="cancel"),
    path("add/<int:pk>",views.add,name="add")




    
]