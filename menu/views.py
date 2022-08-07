from django.shortcuts import render
from django.views import generic


def index(request):
    context = {
        'add_problem': '添加题目',
        'add_link': '',
        'problems': '浏览题目',
    }
    return render(request, 'menu/index.html', context)
