from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Hello, world. You're at the polls page.</h1>")


def about(request):
    return HttpResponse("<h1>About this page</h1>")
