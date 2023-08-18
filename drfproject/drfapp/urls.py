from django.urls import path
from .views import SignupView, LoginView, LogoutView
from .views import GetCreate
from .views import GetUpdateDelete
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('students', GetCreate.as_view(), name='get-all-students'),
    path('student/<int:id>', GetUpdateDelete.as_view(), name='get-a-student'),
    path('student/<int:id>/edit', GetUpdateDelete.as_view(), name='update-a-student'),
    path('student/<int:id>/delete', GetUpdateDelete.as_view(), name='delete-a-student')

]
