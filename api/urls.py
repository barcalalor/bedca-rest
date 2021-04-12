"""django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter

from api.food.view import FoodViewSet
from api.foodgroup.view import FoodGroupViewSet
from api.componentgroup.view import ComponentViewSet
from api.user.view import UserViewSet

router = DefaultRouter()

router.register("users", UserViewSet, basename="users")
router.register("food", FoodViewSet, basename="food")
router.register("foodgroup", FoodGroupViewSet, basename="foodgroup")
router.register("componentgroup", ComponentViewSet, basename="componentgroup")
