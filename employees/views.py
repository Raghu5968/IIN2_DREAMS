from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
from django.http import JsonResponse
from .forms import CheckInForm
from .models import TimeSheet
from django.http import HttpResponseRedirect
import datetime

from django.http import HttpResponse
from .tasks import *
from django.shortcuts import render
import time
import schedule
from django.utils import timezone



from django.http import HttpResponse

import json

# Create your views here.


def index(request):
    
    return render(request,'index.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateEmpForm()
        if request.method == 'POST':
            form = CreateEmpForm(request.POST)
            if form.is_valid():
                user = form.save()  
                username = form.cleaned_data.get('username')
                
                
                group = Group.objects.get(name='employee')
                user.groups.add(group)
                
               
                Employees.objects.create(user=user, empname=user.username, email=user.email)
                
                messages.success(request, 'User successfully created for ' + username)
                return redirect('register')  

        context = {'form': form}
        return render(request, 'register.html', context)


def Loginpage(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/') 
        else:
            messages.info(request,'empname or password error')
            print("employee_name or password error ")
            return redirect('Loginpage')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('/')



def check_in(request):
    if request.method == 'POST':
       
        ip_address = request.META.get('REMOTE_ADDR')

        
        check_in_instance = Check_in.objects.create(ip_address=ip_address)
        check_in_instance.save()

        return HttpResponse("Checked in successfully!")
    else:
        return HttpResponse("Invalid request method.")

