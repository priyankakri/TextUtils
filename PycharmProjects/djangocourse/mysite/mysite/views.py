# i have created this file -- priyanka

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepuncvar=request.POST.get('removepunc','off')
    fullcapsvar = request.POST.get('fullcaps', 'off')

    if removepuncvar=="on":
        x = ""
        punc="!@#$%^&*(){}[].:;'"
        for i in djtext:
            if i not in punc:
                x=x+i
        params = {'purpose': 'removepunc', 'analyzed_text': x}
        djtext=x
        #return render(request, 'analyze.html', params)

    if fullcapsvar=="on":
        x=""
        for char in djtext:
            x=x+char.upper()
        params={'purpose':'uppercase','analyzed_text':x}

    if(removepuncvar != "on" and fullcapsvar != "on"):
        return HttpResponse("Error : please select any operation and try again")
    else:
        return render(request,'analyze.html',params)
