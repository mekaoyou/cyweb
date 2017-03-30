#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
import logging
from models import CY
from django.core import serializers
import time

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


def detailII(request, cyName):
    log.debug(u'the query id is -> %s', cyName)
    cy = CY.objects.filter(name=cyName)
    return JsonResponse(serializers.serialize("json", cy), safe=False)


def uploadImage(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        try:
            path = "media/article_images/" + time.strftime("%Y%m%d%H%M%S", time.localtime())
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, "wb+")
            for chunk in f:
                des_origin_f.write(chunk)
            des_origin_f.close()
        except Exception, e:
            print log.error(u'the query id is -> %s', e)

        res = r"<script>window.parent.CKEDITOR.tools.callFunction(" + callback + ",'/" + file_name + "', '');</script>"
        return HttpResponse(res)
    else:
        raise Http404()





