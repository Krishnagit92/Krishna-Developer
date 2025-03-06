from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def order_foods(request):
    return render(request, 'order_foods.html')

def register_form_submission(request):
    #request={"method":"post","firstname":john,"lastname":Doe}
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email_id=request.POST.get('email_id')
    phone_number=request.POST.get('phone_number')
    password=request.POST.get('password')
    print(first_name,last_name,email_id,phone_number,password)
    ex1=customer_register_table(first_name=first_name,
                                last_name=last_name,
                                email_id=email_id,
                                phone_number=phone_number,
                                password=password)
    ex1.save()
    print("data saved successfully")
    return render(request, 'login.html')

