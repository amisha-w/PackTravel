from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def publish_index(req):
    return render(req, 'publish/publish.html')