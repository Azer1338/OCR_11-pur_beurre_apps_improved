"""Pur_beurre_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
import debug_toolbar
from django.conf.urls import include, url
from django.contrib import admin
from pur_beurre_project import settings

urlpatterns = [
    url(r'^', include('main.urls'), name="main"),
    url(r'^admin/', admin.site.urls),
    url(r'^substitute/', include('substitute.urls'), name="substitute"),
    url(r'^accounts/', include('accounts.urls'), name="accounts"),
]

if settings.DEBUG:
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
