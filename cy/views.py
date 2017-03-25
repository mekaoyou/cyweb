#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse
import logging
from models import CY
from django.core import serializers

# Create your views here.

log = logging.getLogger('cy.app')


def index(request):
    return render(request, 'cy/index.html')


def query(request, keywords):
    log.debug(u'the query key words is -> %s', keywords)
    cys = CY.objects.filter(name__contains=keywords)
    return JsonResponse(serializers.serialize("json", cys), safe=False)


def detail(request, cyId):
    log.debug(u'the query id is -> %d', int(cyId))
    cy = CY.objects.filter(id=int(cyId))
    return JsonResponse(serializers.serialize("json", cy), safe=False)




