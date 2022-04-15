
from django.http import HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def nav(request):
    return render(request,"index.html")

def analyze(request):
    rawtext=request.GET.get('text')
    pun=request.GET.get('rf')
    uc=request.GET.get('upper')
    space=request.GET.get('space')
    answer=""
    if pun=='true':
        punctuation='''!@#$%^&*()_+<>?/~`'''
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
                answer=answer+ch
    return render(request,'analyze.html',{'ans':answer})