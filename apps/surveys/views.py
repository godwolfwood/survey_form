# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.messages import get_messages
# Create your views here.

def index(request):
    return render(request,'surveys/index.html')

def process(request):
    if request.method == "POST":
        name = request.POST['form_name']
        if len(name) < 1:
            messages.error(request, "Name can't be empty")
        desc = request.POST['form_description']
        if len(desc) < 1:
            desc = ''
        storage = get_messages(request)
        if storage:
            return redirect('/surveys')
        
        location = request.POST['form_location']
        lang = request.POST['form_lang']
        request.session['result'] ={
            "name": name,
            "language": lang,
            "location":location,
            "description": desc
        }
        return redirect('/surveys/result')
    else:
        return redirect('/surveys')

def result(request):
    return render(request,'surveys/result.html')