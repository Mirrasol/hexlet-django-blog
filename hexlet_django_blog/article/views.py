from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'articles/index.html')


def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')
