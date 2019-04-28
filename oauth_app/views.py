from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request,'oauth/login.html')

def profile(request):
    return render(request,'oauth/profile.html')

def logout(request):
    return render (request,'oauth/login.html')