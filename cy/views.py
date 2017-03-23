#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, 'cy/index.html')


def test(request):
    return JsonResponse({'name': 'alex'})



