from http.client import HTTPResponse
from django.shortcuts import render,redirect
from numpy import True_, dtype
import requests
import json
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from publish.forms import RideForm
from utils import get_client

client = None
db = None
userDB = None
ridesDB  = None
routesDB  = None

def intializeDB():
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB  = db.rides
    routesDB  = db.routes

def search_index(request):
    intializeDB()
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    all_rides = list(ridesDB.find())
    all_routes = list(routesDB.find())
    processed, routes = list(), list()
    processed_routes = list()
    for ride in all_rides:
        routes = ride['route_id']
        for route in all_routes:
            if route['_id'] in routes:
                ride.update(route)
        ride['id'] = ride.pop('_id')
        processed.append(ride)
    return render(request, 'search/search.html', {"username": request.session['username'], "rides": processed})
