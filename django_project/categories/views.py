from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django_project.articles.models import Article

from django_project.categories.models import Category




class Index(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()[:15]

        if not categories.exists():
            default_category = [{'name': 'Категорий нет', 'description': '', 'id': 0}]
            return render(request, 'categories/index.html', context={'categories': default_category})
        return render(request, 'categories/index.html', context={'categories': categories})



class Categories_view(View):
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, id=kwargs["id"])
        articles = Article.objects.filter(category=category)
        return render(
            request,
            "categories/category.html",
            context={
                "category": category,
                "articles": articles
            },
        )

