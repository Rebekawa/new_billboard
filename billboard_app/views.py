# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.views.decorators.csrf import csrf_exempt
import datetime

@csrf_exempt
def index(request):
    date = datetime.date.today()
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        author = request.POST.get('author')
        print(title, message, author)
        model = Post(title=title, message=message, author=author)
        model.save()
    context = {}
    posts = Post.objects.all()
    context['messages'] = posts
    context['date'] = date
    print(context)
    return render(request, 'billboard_app/posts.html', context)


def login_form(request):
    if request.method == 'GET':
        return render(request, "registration/login.html")
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print("hello")
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/billboard/')
        else:
            return redirect('/billboard/login/')


def logout_form(request):
    logout(request)
    return render(request, 'registration/logout.html')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return index(request)
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", { "form": form })