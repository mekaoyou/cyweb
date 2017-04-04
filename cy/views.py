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


def about(request):
    well = Welcome.objects.filter(id=2)
    return toJSON(well)


def welcome(request):
    well = Welcome.objects.filter(id=1)
    return toJSON(well)


def query(request, keywords):
    log.debug(u'the query key words is -> %s', keywords)
    cys = CY.objects.filter(name__contains=keywords)
    return toJSON(cys)


def detail(request, cyId):
    log.debug(u'the query id is -> %d', int(cyId))
    cy = CY.objects.filter(id=int(cyId))
    return toJSON(cy)


def detailII(request, cyName):
    log.debug(u'the query id is -> %s', cyName)
    cy = CY.objects.filter(name=cyName)
    return toJSON(cy)


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
    return toJSON(cats)


def arts(request, cat_id):
    log.debug(u'blogs enter and cat id is %s', cat_id)
    cats = Category.objects.filter(parent=int(cat_id))
    cate_ids = [cate.id for cate in cats]
    cate_ids.append(int(cat_id))
    arts = Article.objects.filter(category__in=cate_ids, display=True).order_by('-date_time', 'id')
    return toJSON(arts)


def artList(request):
    log.debug(u'the artList enter')
    arts = Article.objects.filter(display=True).order_by('-date_time', 'id')
    return toJSON(arts)


def art(request, art_id):
    log.debug(u'the art enter id is %s', art_id)
    arts = Article.objects.filter(id=int(art_id), display=True)
    return toJSON(arts)


def artName(request, keywords):
    log.debug(u'the art enter name is %s', keywords)
    arts = Article.objects.filter(title=keywords, display=True)
    return toJSON(arts)


def artQuery(request, keywords):
    log.debug(u'the artQuery keywords is %s', keywords)
    arts = Article.objects.filter(title__contains=keywords, display=True).order_by('-date_time', 'id')
    return toJSON(arts)


def help(request):
    log.debug(u'the help enter')
    helps = Help.objects.filter(display=True).order_by('order')
    return toJSON(helps)


def toJSON(arr):
    return JsonResponse(serializers.serialize("json", arr, use_natural_foreign_keys=True), safe=False)

