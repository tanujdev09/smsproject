
from django.shortcuts import render,redirect;

def FacultyHomePage(request):
    return render(request, 'facultyapp/FacultyHomePage.html')



