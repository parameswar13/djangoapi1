from employee.models import employees
from employee.models import skills
from employee.models import projects
from rest_framework_mongoengine import serializers

class EmployeeSerializer(serializers.DocumentSerializer):
    class Meta:
        model = employees
        fields = "__all__"