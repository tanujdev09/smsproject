from django.contrib import messages
from django.contrib.auth.models import User,auth

from django.shortcuts import render, get_object_or_404


def projecthomepage(request):
    return render(request,'adminapp/projecthomepage.html')
def printpagecall(request):
    return render(request, 'adminapp/printer.html')

def printpagelogic(request):
    if request.method=="POST":
        user_input = request.POST['user_input']
        print(f'user input:{user_input}')
    a1={'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)

def exceptionpagecall(request):
    return render(request,'adminapp/ExceptionExample.html')
def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message=None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request,'adminapp/ExceptionExample.html',{'result':result,'error':error_message})
    return render(request, 'adminapp/ExceptionExample.html')
def UserRegisterpagecall(request):
    return render(request,'adminapp/UserRegisterPage.html')
def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')
def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/Projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegister.html')

from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')

def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')  # Replace with your student homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')  # Replace with your faculty homepage URL name
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/UserLoginPage.html')
    else:
        return render(request, 'adminapp/UserLoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

from .forms import *

def add_task(request):
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form=TaskForm()
        tasks=Task.objects.all()
        return render(request, 'adminapp/add_task.html',{'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

from .forms import StudentForm
from .models import StudentList

def add_students(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')

    else:
        form = StudentForm()
    return render(request, 'adminapp/add_student.html', {'form': form})

def student_list(request):
    students = StudentList.objects.all()
    return render(request,'adminapp/student_list.html',{'students':students})
'''
from .forms import UploadFileForm
import pandas as pd
import matplotlib.pyplot as plt
import base64

def upload_file(request):
    if request.method=='POST' and request.FILES['file']:
        file=request.FILES('file')
        df=pd.read_csv(file, parse_dates=['Date'], dayfirst=True)
        total_sales=df['Sales'].sum()
        average_sales=df['Sales'].mean()

        df['Month'] = df['Date'].dt.month
        monthly_sales=df.groupby('Month') ['Sales'].sum()
        month_names=['Jan','Feb','March','April','May','June','July','Aug','Sep','Oct','Nov','Dec']
        monthly_sales.index=monthly_sales.index
'''

def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')

import datetime
import calendar
from datetime import timedelta

def datetimepagelogic(request):
    if request.method=='POST':
        number1=int (request.POST['date1'])
        x=datetime.datetime.now()
        ran=x + timedelta(days=number1)
        ran1=ran.year
        ran2=calendar.isleap(ran1)
        if ran2==False:
            ran3="Not A Leap Year"
        else:
            ran3="Leap Year"
    a1={'ran': ran, 'ran3': ran3, 'ran1': ran1, 'number1': number1}
    return render(request, 'adminapp/datetimepage.html', a1)

import random
import string

def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')

def randomlogic(request):
    if request.method=="POST":
        number1=int(request.POST['number1'])
        ran=''.join(random.sample(string.ascii_uppercase + string.digits, k=number1))
    a1={'ran':ran}
    return render (request, 'adminapp/randomexample.html',a1)















