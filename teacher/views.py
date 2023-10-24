
from django.http import TttpsResponse
from django.shortcuts import render

# Create your views here.


def Home(request):
    return HttpResponse("welcome to emobilis")
