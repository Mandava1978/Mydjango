from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

# Create your views here.

def myfunctioncall(regquest):
    return  HttpResponse("Hello World!!!")

def myfunctionabout(regquest):
    return  HttpResponse("About - Hello World!!!")

def add(regquest,a,b):
    return  HttpResponse(f"Sum : {a+b}")

def intro(reguest, age, name):
    mydict ={
        "Name" : name,
        "Age" : age
    }
    return JsonResponse(mydict)

 