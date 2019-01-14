# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
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
