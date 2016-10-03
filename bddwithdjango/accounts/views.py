from functools import reduce

import operator
from django.contrib.auth import authenticate, login as dj_login
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Interest, User


def home_page(request):
    interests = Interest.objects.all()
    if request.method == 'POST':
        interests = request.POST.getlist('interests')
        filtered_users = User.objects.filter(reduce(lambda x, y: x | y, [Q(interests__name__contains=word) for word in interests]))
        return render(request, template_name='home.html',
                      context={'interests': interests, 'filtered_users': filtered_users})
    return render(request, template_name='home.html', context={'interests': interests})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect('/')
    return render(request, template_name='login.html')
