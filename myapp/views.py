from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view1(request):
    return HttpResponse('<h1>welcome to view1</h1>')


def view2(request,email):
    return render(request,'sample.html',context={'email':email,'name':'Ajay V Raikar'})

def view3(request,name):
    return HttpResponse(f'<h1>Hello Mr./Ms. {name}</h1>')