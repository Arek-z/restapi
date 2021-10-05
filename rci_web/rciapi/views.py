from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Unit, Employee
from rest_framework import viewsets
from .serializer import EmployeeSerializer, UnitSerializer


class UnitViewSet(APIView):
    def post(self, request):

        serializer = UnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #queryset = Unit.objects.all()
    #serializer_class = UnitSerializer


class EmployeeViewSet(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #queryset = Employee.objects.all()
    #serializer_class = EmployeeSerializer


# Create your views here.
