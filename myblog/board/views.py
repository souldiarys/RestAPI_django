from django.shortcuts import render

def post_list(request):
    context = {}
    return render(request, 'post_list.html', context)