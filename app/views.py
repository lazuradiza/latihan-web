from django import http
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def landing_page(request):
    return HttpResponse("hai lazu gantenk")

def second_page(request):
    return HttpResponse("jiancuk kon")

def profile(request):
    return HttpResponse("profile lazu")

def count(request,angka):
    angka = angka+1
    return HttpResponse(str(angka))

def example(request):
    return render(request, 'example.html')