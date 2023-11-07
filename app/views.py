from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def jamPandu(request):
    return HttpResponse ("<h1><marquee>Hello Jampandu How are you</h1></marquee>")

def greet(request):
    return HttpResponse ("<h1><marquee>Hello welcome to the webApplication</h1></marquee>")

def welcome(request):
    return HttpResponse ("<h1>Hey Everyone this is the third function of application<h1>") 