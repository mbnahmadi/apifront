from multiprocessing import context
from urllib import response
from django.shortcuts import render
import requests
from django.http import HttpResponse
# import json
# Create your views here.




def show(request):
    response = requests.get('http://127.0.0.1:8001/api/0')
    r = response.json()
    context = {"api" : r,
               }
    # html = '<html><body>%s</body></html>' %r
    return render(request , "test.html" , context)
    

