#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
import logging
from models import CY, Category, Article, Welcome, Help
from django.core import serializers
import time

# Create your views here.

log = logging.getLogger('cy.app')


def index(request):
    well = Welcome.objects.get(id=1)
    return render(request, 'cy/index.html', {'SHELL': well.shell, 'TITLE': well.title})


def welcome(request):
    well = Welcome.objects.all()
    return JsonResponse(serializers.serialize("json", well), safe=False)


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


def category(request):
    log.debug(u'the category enter')
    cats = Category.objects.all()
    return JsonResponse(serializers.serialize("json", cats), safe=False)


def blogs(request, cat_id):
    log.debug(u'blogs enter and cat id is %s', cat_id)
    blogs = Article.objects.filter(category=int(cat_id))
    return JsonResponse(serializers.serialize("json", blogs, use_natural_foreign_keys=True), safe=False)


def artList(request):
    log.debug(u'the artList enter')
    arts = Article.objects.all()
    return JsonResponse(serializers.serialize("json", arts), safe=False)


def art(request, art_id):
    log.debug(u'the art enter id is %s', art_id)
    arts = Article.objects.filter(id=int(art_id))
    return JsonResponse(serializers.serialize("json", arts, use_natural_foreign_keys=True), safe=False)


def artQuery(request, keywords):
    log.debug(u'the artQuery keywords is %s', keywords)
    arts = Article.objects.filter(title__contains=keywords)
    return JsonResponse(serializers.serialize("json", arts, use_natural_foreign_keys=True), safe=False)


def help(request):
    log.debug(u'the help enter')
    helps = Help.objects.filter(display=True)
    return JsonResponse(serializers.serialize("json", helps), safe=False)

