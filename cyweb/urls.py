#!/usr/bin/python
# -*- coding: utf-8 -*-

"""cyweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from cy import views as cy
from django.views.static import serve

admin.site.site_header = u'Blog管理'
admin.site.site_title = u'Blog管理'

urlpatterns = [
    url(r'^$', cy.index),
    url(r'^wellcome/', cy.wellcome),
    url(r'^query/(?P<keywords>.+)/$', cy.query),
    url(r'^detail/(\d+)/$', cy.detail),
    url(r'^detail/([^ -~]+)/$', cy.detailII),
    url(r'^cate/(\d+)/$', cy.blogs),
    url(r'^cate/', cy.category),
    url(r'^art/(\d+)/$', cy.art),
    url(r'^arts/(?P<keywords>.+)/$', cy.artQuery),
    url(r'^arts/', cy.artList),
    url(r'^admin/', admin.site.urls),
    url(r'^uploadimg/', cy.uploadImage),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
]

