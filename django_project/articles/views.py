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
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from .models import Article
from django.views import View
from .forms import ArticleCreateForm


# class ArticleFormView(View):

#     def post(self, request, *args, **kwargs):
#         form = ArticleCreateForm(request.POST)  # Получаем данные формы из запроса
#         if form.is_valid():  # Проверяем данных формы на корректность
#             form.save()  # Сохраняем форму
#         return redirect('articles_index')
#     def get(self, request, *args, **kwargs):
#         form = ArticleCreateForm()  # Создаем экземпляр нашей формы
#         return render(
#             request, "articles/article_create.html", {"form": form}
#         )  # Передаем нашу форму в контексте


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
    

@require_http_methods(['GET', 'POST'])
def article_create(request):
    if request.method == 'POST':
        form = ArticleCreateForm(request.POST)  # Получаем данные формы из запроса
        if form.is_valid():  # Проверяем данных формы на корректность
            form.save()  # Сохраняем форму
        return redirect('articles_index')
    form = ArticleCreateForm()  # Создаем экземпляр нашей формы
    return render(
        request, "articles/article_create.html", {"form": form}
    )  # Передаем нашу форму в контексте

@require_http_methods(['GET','POST'])
def article_update(request, id):
    if request.method == 'POST':
        article = Article.objects.get(id=id)
        form = ArticleCreateForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
        return redirect('articles_index')
    article = Article.objects.get(id=id)
    form = ArticleCreateForm(instance=article)
    return render(
            request, "articles/article_update.html", {"form": form, "article_id": id}
        )

# @require_http_methods(['POST'])
def article_detete(request, id):
    article = Article.objects.get(id=id)
    if article:
        article.delete()
    return redirect("articles_index")


# @require_http_methods(['POST'])
# def update_article(request, id):
#     try:
#         article = Article.objects.get(id=id)


