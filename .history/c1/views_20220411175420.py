import imp
from django.http import HttpResponse
from django.shortcuts import render
from . import urls
from django.http import HttpResponse
# Create your views here.

def nav(request):
    return HttpResponse("hello")
