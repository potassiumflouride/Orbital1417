"""orbital1417 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from .import views as main_views

urlpatterns = [
    #url(r'^$', admin.site.urls), #homepage
    #url(r'^$',main_views.homePage, name='homepage'), # problem cannot make homepage
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('homepage.urls')),
    url(r'^charity/', include('charity.urls')),
    url(r'^pairing/', include('pairing.urls')),
    url(r'^userAcc/', include('userAcc.urls')),
    url(r'^tracklah/', include('tracklah.urls')),
]
