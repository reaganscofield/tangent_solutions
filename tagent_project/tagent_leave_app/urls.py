from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('employeers', views.EmployeeViews)
router.register('leaves', views.LeaveViews)

urlpatterns = [
    path('', include(router.urls)),
]
