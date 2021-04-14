from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view1(request):
    return HttpResponse('<h1>welcome to view1</h1>')


def view2(request,email):
    return render(request,'sample.html',context={'email':email,'name':'Ajay V Raikar'})

def view3(request,name):
    return HttpResponse(f'<h1>Hello Mr./Ms. {name}</h1>')

def if_demo(request):
    login = True
    return render(request,'if_demo.html',context={'login':login})

def ifelse_demo(request):
    login = False
    return render(request,'ifelse_demo.html',context={'login':login,'name':'Ajayvraikar','a':10,'b':50})

def for_demo(request):
    return render(request,'for_demo.html',context={'items':['apple','ball','cat'],'profile':{'name':'Ajayvraikar','age':22,'salary':24000}})