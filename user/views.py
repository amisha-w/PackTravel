from http.client import HTTPResponse
from django.shortcuts import render,redirect
import requests
import json
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from utils import get_client
from django.http import HttpResponse

# Home page for PackTravel
def index(request):
    try:
        client = get_client()
    except:
        return HttpResponse("Error!")
    return render(request, 'home/home.html')


def home(request):
    return render(request, 'home/home.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'user/register.html', context)