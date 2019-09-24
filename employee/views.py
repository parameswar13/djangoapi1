from rest_framework_mongoengine import viewsets as meviewsets

from employee.models import employees
from employee.serializers import EmployeeSerializer

class EmployeesView(meviewsets.ModelViewSet):
    lookup_field = 'empId'
    queryset = employees.objects.all()
    serializer_class = EmployeeSerializer

