from django.shortcuts import render
from django.views import View
from .models import Article
from django.db.models import Q


class HomePage(View):
    def get(self, request):
        articles_list = Article.objects.exclude(
            Q(is_draft=True) | Q(is_deleted=True)
        ).values()
        context = {
            'articles_list': articles_list
        }
        print(Article.objects.exclude(
            Q(is_draft=True) | Q(is_deleted=True)
        ).all()) 
        return render(request, 'blog/index.html', context)
