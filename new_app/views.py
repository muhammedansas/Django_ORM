from django.shortcuts import render
from . models import Student,Book,Store,Department,Employees
from django.db.models import Q,Sum,F
from django.db.models.functions import Length


# Create your views here.

def home(request): 
    new = Student.objects.filter(name__icontains = 'ansas')
    for i in new:
        print(i.name)
    
    return None