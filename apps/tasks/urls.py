from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    path('', views.TaskListView.as_view(), name='list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='detail'),
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='delete'),
    path('<int:task_id>/finish/', views.finish_task, name='finish'),
    path('<int:task_id>/unfinish/', views.unfinish_task, name='unfinish'),
]