from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

from .forms import LoginForm, JoinForm

# Create your views here.
def login(request):
    context = {'login_form': LoginForm()}
    return render(request, 'login.html', context)

def login_validate(request):
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        user = auth.authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('board:post_list')
            else:
                return HttpResponse('사용자가 비활성화되어 있습니다.')
        else:
            return HttpResponse('사용자가 없거나 비밀번호가 틀렸습니다.')
    else:
        return HttpResponse('로그인 폼이 비정상적입니다.')

def join_page(request):
    if request.method == 'POST':
        join_form_data = JoinForm(request.POST)
        if join_form_data.is_valid():
            username = join_form_data.cleaned_data['id']
            password = join_form_data.cleaned_data['password']
            User.objects.create_user(username=username, password=password)
            return redirect('user:login')
    else:
        join_form_data = JoinForm()

    context = {'join_form': join_form_data}
    return render(request, 'join_page.html', context)