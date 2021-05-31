from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/validate', views.login_validate, name='login_validate'),
]