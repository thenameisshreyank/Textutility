
from django.http import HttpResponse
from django.shortcuts import render
from templates import *
from django.http import HttpResponse
# Create your views here.

def nav(request):
    return render(request,"templates/index.html")