
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def nav(request):
    return render(request,"index.html")

def analyze(request):
    rawtext=request.GET.get('text')
    print(rawtext)
    return render(request,'analyze.html',{'ans':rawtext})