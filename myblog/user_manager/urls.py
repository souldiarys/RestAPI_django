from django.urls import path

from .views import login, login_validate, join_page

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('login/validate', login_validate, name='login_validate'),
    path('join/', join_page, name='join_page'),
]