from django.views.generic import ListView
from .models import Image
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render


class HomeView(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'home.html'


def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    return render(request, "/")
