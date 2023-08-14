from django.urls import path
from .views import GetCreate
from .views import GetUpdateDelete

urlpatterns = [
    path('students', GetCreate.as_view(), name='get-all-students'),
    path('student/<int:id>', GetUpdateDelete.as_view(), name='get-a-student'),
    path('student/edit/<int:id>', GetUpdateDelete.as_view(), name='update-a-student'),
    path('student/<int:id>/delete', GetUpdateDelete.as_view(), name='delete-a-student')

]
