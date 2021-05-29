from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post

def post_list(request):
    post_list = Post.objects.all()

    page = request.GET.get('page', '1')
    paginator = Paginator(post_list, 2)
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page}
    return render(request, 'post_list.html', context)