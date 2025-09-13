# from django.shortcuts import render
# from django.views import View




# # def index(request):
# #     return render(request, 'articles/index.html', context={'articles': articles})

# class index(View):
#     template_name = "articles/index.html"
    
#     def get(self, request, tags='python', article_id=42):
#         return render(request,
#                       'articles/index.html',
#                       context={
#                           'articles': articles,
#                           'tags': tags,
#                           'article_id': article_id,
#                         },
#                     )

from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Article


@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        Article.objects.create(
            title=request.POST['title'],
            author=request.POST['author']
        )
        articles = Article.objects.all()
        return render(request, 'articles/index.html', context={'articles': articles})

    articles = Article.objects.all()
    if not articles.exists():
        default_article = [{'title': 'Статей нет', 'author': '', 'id': 0}]
        return render(request, 'articles/index.html', context={'articles': default_article})
    return render(request, 'articles/index.html', context={'articles': articles})


@require_http_methods(['GET'])
def article_view(request, id):
    try:
        article = Article.objects.get(id=id)
        return render(request, 'articles/article.html', context={'article': article})
    except Article.DoesNotExist:
        raise Http404("Статья не найдена.")

# @require_http_methods(['POST'])
# def update_article(request, id):
#     try:
#         article = Article.objects.get(id=id)


