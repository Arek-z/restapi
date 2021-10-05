from django.urls import include, path
from rest_framework import routers
from .views import UnitViewSet, EmployeeViewSet


urlpatterns = [
    path('units/', UnitViewSet.as_view()),
    path('employees/', EmployeeViewSet.as_view())
]
