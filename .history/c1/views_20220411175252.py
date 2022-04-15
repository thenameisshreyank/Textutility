from django.http import HttpResponse
from django.shortcuts import render
from . import urls
# Create your views here.

def nav(request):
    return HttpResponse("hello")
