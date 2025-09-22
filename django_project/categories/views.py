from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django_project.articles.models import Article
from django_project.categories.forms import CategoryForm
from django_project.categories.models import Category




class Index(View):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()[:15]

        if not categories.exists():
            default_category = [{'name': 'Категорий нет', 'description': '', 'id': 0}]
            return render(request, 'categories/index.html', context={'categories': default_category})
        return render(request, 'categories/index.html', context={'categories': categories})



class Category_view(View):
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
    
class CategoryFormView(View):

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_index')
        return render(request, 'categories/category_create.html', {'form': form})

    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, 'categories/category_create.html', {'form': form})


class Category_update(View):
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get('id')
        category = Category.objects.get(id=category_id)
        form = CategoryForm(instance=category)
        return render(
            request, 'categories/category_update.html', {'form': form, 'category_id': category_id}
        )

    def post(self, request, *args, **kwargs):
        category_id = kwargs.get('id')
        category = Category.objects.get(id=category_id)
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_index')

        return render(
            request, 'categories/category_update.html', {'form': form, 'category_id': category_id}
    )


class Category_delete(View):
    def post(self, request, *args, **kwargs):
        category_id = kwargs.get("id")
        category = Category.objects.get(id=category_id)
        if category:
            category.delete()
        return redirect("categories_index")
