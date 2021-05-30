from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import auth

from .models import Post
from .forms import LoginForm

def post_list(request):
    post_list = Post.objects.all()

    page = request.GET.get('page', '1')
    paginator = Paginator(post_list, 2)
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page}
    return render(request, 'post_list.html', context)

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