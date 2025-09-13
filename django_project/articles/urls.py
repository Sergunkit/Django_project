from django.urls import path
from django_project.articles import views
from django_project.articles.views import index

urlpatterns = [
    # path('', index.as_view(template_name='index.html'), name='articles_index'),
    # path('<str:tags>/<int:article_id>', index.as_view(template_name='index.html'), name='article_detail'),
    path('', views.index, name='articles_index'),
    path('<int:id>', views.article_view, name='article_detail'),
]


