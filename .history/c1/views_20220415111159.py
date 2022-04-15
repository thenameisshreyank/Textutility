
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def nav(request):
    return render(request,"index.html")

def analyze(request):
    rawtext=request.POST.get('text')
    pun=request.POST.get('rf')
    uc=request.POST.get('upper')
    space=request.POST.get('space')
    answer=""
    ans1=""
    if pun=='true':
        punctuation='''!@#$%^&*()_;+<>?/~`"='''
        for x in rawtext:
            if x not in punctuation:
             answer=answer+x
    else:
        answer=rawtext
    if uc=="true":
        # for ch in rawtext:
        answer=answer.upper()

    if space=="true":
        for ch in answer:
            if ch==" ":
                pass
            else:
                ans1=ans1+ch
        answer=ans1
    return render(request,'analyze.html',{'ans':answer})