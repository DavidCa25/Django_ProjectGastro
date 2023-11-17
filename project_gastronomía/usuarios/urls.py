from . import views
from django.urls import path

app_name="usuarios"
urlpatterns = [
    path('', views.LoginView.as_view(), name='usuarios_login'),
    path('new/', views.CreateView.as_view(), name='usuarios_create'),
]