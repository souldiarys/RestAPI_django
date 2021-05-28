from django.http.response import HttpResponse
from django.shortcuts import render

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin

from .models import Post
from .serializers import PostSerializer

# Create your views here.
def blog_page(request):
    post_list = Post.objects.all()

    return HttpResponse('Hello! ' + post_list[0].title)

class blog_api(GenericAPIView, ListModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
