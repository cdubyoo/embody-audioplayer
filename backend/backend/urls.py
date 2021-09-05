"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from audio import views

# router maps incoming reqeust to viewset based on method type
router = routers.DefaultRouter()
router.register(r'audios', views.AudioView, 'audio')
router.register(r'comments', views.CommentView, 'comment')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # specifies the API url path
]
