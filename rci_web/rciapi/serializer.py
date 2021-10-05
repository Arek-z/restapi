from rest_framework.relations import SlugRelatedField

from .models import Unit, Employee
from rest_framework import serializers


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['ou', 'abbr', 'name']



class EmployeeSerializer(serializers.ModelSerializer):

    ou = SlugRelatedField(
        many=False,
        queryset=Unit.objects.all(),
        slug_field='ou'
    )

    class Meta:
        model = Employee
        fields = ['employee_number', 'ou',  'pesel', 'firstname', 'lastname', 'mail', 'phone', 'work_length',
                  'salary']
