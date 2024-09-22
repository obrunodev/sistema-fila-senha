from django.urls import path
from apps.departments import views


app_name = 'departments'
urlpatterns = [
    path('call/', views.department_call, name='call'),
    path('manage/', views.manage_queue, name='manage'),
]
