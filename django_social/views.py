from django.views.generic import ListView
from .models import Image
'''
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
'''


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'
