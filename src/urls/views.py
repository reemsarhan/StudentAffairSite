from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    context = {}
    return render(request, 'index.html', context)


def login(request):
    context = {}
    return render(request, 'login.html', context)
