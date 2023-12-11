from django.urls import path

from employees import views

urlpatterns = [
    path('/register', views.Employee.as_view(), name='index'),
]
