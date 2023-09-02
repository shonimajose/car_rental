from django.urls import path
from .import views

urlpatterns = [
    path("",views.Index,name="Index"),
    path("SignIn",views.SignIn,name="SignIn"),
    path("SignUp",views.SignUp,name="SignUp"),
    path("SignOut",views.SignOut,name ="SignOut"),
    path("AdminIndex",views.AdminIndex,name="AdminIndex"),
    path("log/<int:pk>",views.log,name="log"),
    path("activate/<int:pk>",views.activate,name="activate"),
    path("con",views.con,name="con"),
    path("search",views.search,name="search")


    
]
