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



def source(request):
    # response = requests.get('http://127.0.0.1:8001/api/0')
    # r = response.json()
    # context = {"api" : r,
    #            }
    # # html = '<html><body>%s</body></html>' %r
    return render(request , "source.html" , {})
    

def TableView(request):
    response = requests.get('http://127.0.0.1:5000/api/0')
    r = response.json()
    # html = '<html><body>%s</body></html>' %r
    keys = r[0].keys()
    val = []
    for i, item in enumerate(r):
        val.append([])
        for key in keys:
            val[i].append(item[key])
    print(val)
    context={
        "api" : r,
        "keys": keys,
        "val": val,
    }
    return render(request, "html.html", context)