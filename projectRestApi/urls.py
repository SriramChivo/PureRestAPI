"""projectRestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from pureDjangoApi.views import (serilazedobj, jsonRes, serilazedLisrobj,
                                 serilazedLisrobjLimit, serilazedobjLimit, bestJsonQueryset, restdetailview)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('obj/', serilazedobj.as_view(), name="serobj"),
    path('sample/', jsonRes.as_view(), name="serobj"),
    path('list/', serilazedLisrobj.as_view(), name="serobj"),
    path('listLimit/', serilazedLisrobjLimit.as_view(), name="serobj"),
    path('Api/sampleLimit/', serilazedobjLimit.as_view(), name="serobj"),
    path('Api/best/', bestJsonQueryset.as_view(), name="serobj"),
    re_path(r'Api/(?P<id>\d+)/$', restdetailview.as_view(), name="serobj"),
    re_path(r'^api/', include('pureDjangoApi.Api.urls')),
]
