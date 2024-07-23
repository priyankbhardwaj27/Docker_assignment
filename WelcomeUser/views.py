from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def greetUser(request):
    return HttpResponse('A basic python app using Django framework')
