from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, View
from django.views import View

from .models import Image


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'
