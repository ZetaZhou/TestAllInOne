"""TestReport URL Configuration

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
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from TestReport import views as main_url

urlpatterns = [
    url(r'', admin.site.urls),
    url('gettestreportlist/', main_url.getTestreportList),
    url('gettestreporttemplate/', main_url.getTestreportTemplate),
    url('gettestreportdetail/', main_url.getTestreportDetail),
    url('publishtestreport/', main_url.publishTestreport),
    url('getpublishstatu/', main_url.getpublishstatu)
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
