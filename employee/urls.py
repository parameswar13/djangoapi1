from rest_framework_mongoengine import routers
from employee.views import EmployeesView

router = routers.DefaultRouter()
router.register(r'employee', EmployeesView)

urlpatterns = []
urlpatterns += router.urls
