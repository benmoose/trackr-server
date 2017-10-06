"""trackr URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views

from apps.user.views import UserViewsets
from apps.charge.views import ChargeViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewsets)
router.register(r'charges', ChargeViewSet, base_name='charge')

auth = [
    url(r'^token/?$', views.obtain_auth_token),
]

api_routes = [
    url(r'^auth/', include(auth)),
] + router.urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(api_routes))
]
