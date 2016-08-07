"""quotator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.quotes_home), name='quotes_home'),

    url(r'^add$', login_required(views.quote_create), name='quote_create'),
    url(r'^edit/(?P<quote_id>[0-9]+)$', login_required(views.quote_edit),
        name='quote_edit'),
    url(r'^delete/(?P<quote_id>[0-9]+)$', login_required(views.quote_delete),
        name='quote_delete'),

]
