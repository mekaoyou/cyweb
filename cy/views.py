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
    print [cy for cy in cys]
    # for cy in cys:
    #     print cy
    # log.debug(u'the query result -> %s', cys)
    return JsonResponse(serializers.serialize("json", cys), safe=False)



