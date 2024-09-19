from apps.users import views
from django.urls import include, path

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('update/', views.user_update, name='update'),
]

