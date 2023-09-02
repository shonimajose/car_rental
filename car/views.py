from django.shortcuts import render,redirect
from .forms import CarAddForm
from django.contrib import messages
from .models import CarDetail
from Booknow.models import Book,BookedCar
from django.contrib.auth.decorators import login_required




@login_required(login_url="SignIn")
def CarAdd(request):
    form = CarAddForm()
    if request.method == "POST":
        form = CarAddForm(request.POST,request.FILES)
        if form.is_valid():
            product =form.save()
            product.Owner = request.user
            product.save()
            messages.info(request,"Car Added to list")
            return redirect('CarAdd')
    return render(request,'admin/addcar.html',{"form":form})

@login_required(login_url="SignIn")
def ViewCarlist(request):
       items = CarDetail.objects.all()
       context ={
            "items":items
        }
       return render(request,'admin/carlist.html',context)

def UpdateCar(request,pk):
    car = CarDetail.objects.filter(CarId =pk)
    if request.method=="POST":
        pname= request.POST['pname']
        pbrand= request.POST['pbrand']
        pdis= request.POST['pdis']
        pprice= request.POST['pprice']
        img= request.FILES['img']

        item=CarDetail.objects.get(CarId = pk)

        item.Car_Name = pname
        item.Car_Brand = pbrand
        item.Car_Discription = pdis
        item.Car_Rent = pprice
        item.Car_Image.delete()
        item.Car_Image = img
        item.save()

        messages.info(request,"item updated")


        return redirect("UpdateCar",pk=pk)
    context={
        "car":car  
    }

    return render(request,'admin/updatecar.html',context)

def DeleteCar(request,pk):
    product = CarDetail.objects.get(CarId =pk)
    product.Car_Image.delete()
    product.delete()
    messages.info(request,"Product Deleted")

    return redirect('ViewCarlist')

@login_required(login_url="SignIn")
def ViewCar(request,pk):
    product =CarDetail.objects.filter(CarId =pk)
    context = {
            "product":product
    }
    return render(request,'Viewcar.html',context)

@login_required(login_url="SignIn")
def ViewAll(request):
    if 'Search' in request.GET:
        car= request.GET['Search']
        if car.isdigit():
            product=CarDetail.objects.filter(Car_Rent__lte=car)
        else:
            product=CarDetail.objects.filter(Car_Name=car)
            
             
        
    else:
        product =CarDetail.objects.all()
    context = {
        "product":product
    }
    return render(request,'viewall.html',context)

def ViewOrder(request):
        
        products = BookedCar.objects.all()
        context={
             "items":products

        }
        
        return render(request,'admin/vieworder.html',context)


def IdProof(request,pk):
     item = Book.objects.get(id =pk)
     proof=item.Id_Proof
     context={
          "proof":proof
     }
 
     return render(request,'admin/idproof.html',context)


    
     


# Create your views here.
