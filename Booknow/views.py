from django.shortcuts import render
from django.shortcuts import render,redirect
from .forms import BookAddForm
from django.contrib import messages
from car.models import CarDetail
from .models import Book,BookedCar
from django.conf import settings
import razorpay
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


razorpay_client = razorpay.Client(auth =(settings.RAZOR_KEY_ID,settings.RAZOR_KEY_SECRET))

@login_required(login_url="SignIn")
def BookNow(request,pk):
    car = CarDetail.objects.get(CarId = pk)

    form = BookAddForm()
    if request.method == "POST":
        form = BookAddForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.car= car
            product.user=request.user
            product.save()
            id = product.id
            
            return redirect('Order',pk = id)
            

    return render(request,'book.html',{"form":form, "pk":pk})
@login_required(login_url="SignIn")
def Order(request,pk):
    item= Book.objects.filter(id=pk)
    item1= Book.objects.get(id=pk)
    rent= item1.car.Car_Rent * item1.numberofdays
    id= pk
 
    context={
        
        "product":item ,
        "pk":id,
        "rent":rent
        

        

        
        }
        
        
        
    
    return render(request,'order.html',context)

@login_required(login_url="SignIn")
def Placeorder(request,pk):
    pro= Book.objects.filter(id=pk)
    item= Book.objects.get(id=pk)
    total= item.car.Car_Rent * item.numberofdays
    pitem = BookedCar.objects.create(book = item, user =request.user ,TotalRent=total)
    pitem.save()
    
    currency ='INR'
    amount = total * 100
    razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture=0))
    razorpay_order_id = razorpay_order["id"]
    callback_url = 'paymenthandler/'

    context={
        "product":pro ,

        "total":total,
        "razorpay_order_id":razorpay_order_id,
        "razorpay_merchant_key":settings.RAZOR_KEY_ID,
        "razorpay_amount":amount,
        'currency':currency,
        'callback_url':callback_url,
        'slotid':"1"
    }

    return render(request,"payment.html",context)

@csrf_exempt
def paymenthandler(request):
    if request.method == "POST":
        try:
            payment_id = request.POST.get('razorpay_payment_id','')
            razorpay_order_id = request.POST.get("razorpay_order_id","")
            signature = request.POST.get('razorpay_signature','')
            params_dict={
                "razorpay_order_id":razorpay_order_id,
                "razorpay_payment_id":payment_id,
                "razorpay_signature":signature


            }
            result = razorpay_client.utility.verify_razorpay_signature(params_dict)
            if result is not None:
                amount = 4000
                razorpay_client.payment.capture(payment_id,amount)
                return HttpResponse("Payment Done")
            else:
                return HttpResponse('Done')
        except:
            car = BookedCar.objects.filter(user = request.user,paymentstatus= False)
            car.paymentstatus = True
            car.save()
            return HttpResponse("Not Done")
        
@login_required(login_url="SignIn")
def Booking(request):
    products = BookedCar.objects.all()
    context={
        "items":products

    }

    return render(request,'booking.html',context)

def cancel(request,pk):
    car = BookedCar.objects.get(id =pk,cancel= False)
    car.cancel = True
    car.save()
    return redirect('Booking')

def add(request):
    add = BookedCar.objects.get(all)
    context={
        "add":add
    }


    return render(request,"add.html",context)
# Create your views here.
