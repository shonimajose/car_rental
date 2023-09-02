from django.contrib.auth.models import Group
from django.shortcuts import redirect
from django.http import HttpResponse



def admin_only(view_func):
    def Wrapper_func(request,*args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == None:
            return view_func(request, *args, **kwargs)
        if group == "Vendor":
            return view_func(request, *args, **kwargs)
        if group == "owner": 
            return redirect('AdminIndex')
    return Wrapper_func

def unauthenticated_user(views_fun):
    def warapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect("Index")
        else:
            return views_fun(request,*args,**kwargs)
    return warapper_func

def allowed_user(views_fun):
    def warapper_func(request,*args,**kwargs):
       if request.user.groups.exists():
            group = request.user.groups.all()[0].name
       if group=="Vendor":
            return HttpResponse("Not Allowed")
       if group=="owner":
            return views_fun(request,*args,**kwargs)
    return warapper_func
