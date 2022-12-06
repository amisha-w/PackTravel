from http.client import HTTPResponse
from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from utils import get_client
from .forms import RegisterForm, LoginForm

client = None
db = None
userDB = None
ridesDB = None
routesDB = None


def intializeDB():
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB = db.rides
    routesDB = db.routes


# Home page for PackTravel
def index(request, username=None):
    intializeDB()
    if request.user.is_authenticated:
        request.session["username"] = request.user.username
        request.session['fname'] = request.user.first_name
        request.session['lname'] = request.user.last_name
        request.session['email'] = request.user.email
        user = userDB.find_one({"username": request.user.username})
        if not user:
            userObj = {
                "username": request.user.username,
                "fname": request.user.first_name,
                "lname": request.user.last_name,
                "email": request.user.email,
                "rides": []
            }
            userDB.insert_one(userObj)
            print("User Added")
        else:
            print("User Already exists")
            print(f'Username: {user["username"]}')
        return render(request, 'home/home.html', {"username": request.session["username"]})
    if request.session.has_key('username'):
        return render(request, 'home/home.html', {"username": request.session["username"]})
    return render(request, 'home/home.html', {"username": None})


def register(request):
    intializeDB()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            userObj = {
                "username": form.cleaned_data["username"],
                "unityid": form.cleaned_data["unityid"],
                "fname": form.cleaned_data["first_name"],
                "lname": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email"],
                "password": form.cleaned_data["password1"],
                "phone": form.cleaned_data["phone_number"],
                "rides": []
            }
            userDB.insert_one(userObj)
            request.session['username'] = userObj["username"]
            request.session['unityid'] = userObj["unityid"]
            request.session['fname'] = userObj["fname"]
            request.session['lname'] = userObj["lname"]
            request.session['email'] = userObj["email"]
            request.session['phone'] = userObj["phone"]
            return redirect(index, username=request.session["username"])
        else:
            print(form.errors.as_data())
    else:
        if request.session.has_key('username'):
            return index(request, request.session['username'])
        form = RegisterForm()
    return render(request, 'user/register.html', {"form": form})


def logout(request):
    try:
        request.session.clear()
    except:
        pass
    return redirect(index)


# @describe: Existing user login
def login(request):
    intializeDB()
    if request.session.has_key('username'):
        return redirect(index, {"username": request.session['username']})
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                passw = form.cleaned_data["password"]
                user = userDB.find_one({"username": username})

                if user and user["password"] == form.cleaned_data["password"]:
                    request.session["username"] = username
                    request.session['unityid'] = user["unityid"]
                    request.session['fname'] = user["fname"]
                    request.session['lname'] = user["lname"]
                    request.session['email'] = user["email"]
                    request.session["phone"] = user["phone"]
                    return redirect(index, request.session['username'])

        form = LoginForm()
        return render(request, 'user/login.html', {"form": form})


def my_rides(request):
    intializeDB()
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    all_routes = list(routesDB.find())
    user_list = list(userDB.find())
    final_user, processed = list(), list()
    for user in user_list:
        if request.session["username"] == user['username']:
            final_user = user
    user_routes = final_user['rides']
    for route in all_routes:
        for i in range(len(user_routes)):
            if user_routes[i] == route['_id']:
                route['id'] = route['_id']
                processed.append(route)

    return render(request, 'user/myride.html', {"username": request.session['username'], "rides": processed})


def delete_ride(request, ride_id):
    intializeDB()
    user = userDB.find_one({"username": request.session['username']})
    if user is None:
        pass
    routesDB.delete_one({"_id": ride_id})
    return redirect("/myrides")

