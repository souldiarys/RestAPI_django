from django.urls import path

from . import views

app_name = 'board'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login/', views.login, name='login'),
    path('login/validate', views.login_validate, name='login_validate'),
]