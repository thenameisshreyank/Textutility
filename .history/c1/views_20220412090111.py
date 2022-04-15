
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def nav(request):
    return render(request,"index.html")

def analyze(request):
    rawtext=request.GET.get('text')
    pun=request.GET.get('rf')
    answer=""
    if pun==true:
        punctuation='''!@#$%^&*()_+<>?/~`'''
        for x in rawtext:
            if x not in punctuation:
             answer=answer+x

    return render(request,'analyze.html',{'ans':answer})