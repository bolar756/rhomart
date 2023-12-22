from django.shortcuts import render,redirect
from  .models import Register
from django.contrib import messages
import time
# Create your views here.
def index(request):
    sent=Register.objects.all()     
    return render(request,"head.html",{'sent':sent})
def register(request):
    if request.method=="POST":
       name=request.POST['name']
       amount=request.POST['amount']
       age = request.POST['age']
       catgeory = request.POST['category']
       gender = request.POST['gender']
       obj=Register.objects.create(name=name,amount=amount,age=age,
                               category=catgeory,gender=gender,Date=time.ctime())
       obj.save()
       messages.info(request,'sucessful addition')
       return redirect('/')
    else:
        return redirect('/')