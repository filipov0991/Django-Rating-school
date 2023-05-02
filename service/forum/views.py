from django.http import HttpResponse
from django.shortcuts import render


def index(req):
    print(req.user)
    return render(req, 'forum/index.html')

def about(req):
    return render(req, 'forum/about.html')

def guidelines(req):
    return render(req, 'forum/guidelines.html')
