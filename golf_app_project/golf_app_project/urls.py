"""
URL configuration for golf_app_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import path, include
from golf_app.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView
)
router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'rounds', RoundViewSet)
router.register(r'holes', HoleViewSet)
router.register(r'scores', ScoreViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('create-user/', create_user),
    path('profile/', get_profile),
    path('token/', TokenObtainPairView.as_view()),

]
