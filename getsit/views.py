from django.http.response import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'getsit/home.html')

def about(request):
    return render(request, 'getsit/about.html')