from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def test_one(request):
    return HttpResponse('<marquee><h1>the string is short</h1></marquee')