from django.shortcuts import render
from django.views import View
from article.models import Category, News

# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html', {
            'categories': Category.objects.filter(status=True),
            'newses': News.objects.filter(status=True),
            'nav_cats': Category.objects.filter(status=True)[0:7],
            'latest_news': News.objects.filter(status=True).order_by('-id')[0:3]
        })


class CategoryView(View):
    def get(self, request, slug):
        return render(request, "category.html", {
            'categories': Category.objects.filter(status=True),
            'category': Category.objects.get(slug=slug),
            'nav_cats': Category.objects.filter(status=True)[0:7],
        })


class NewsView(View):
    def get(self, request, slug):
        return render(request, "news.html", {
            'news': News.objects.get(slug=slug, status=True),
            'nav_cats': Category.objects.filter(status=True)[0:7],
        })