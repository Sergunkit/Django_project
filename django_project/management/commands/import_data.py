from django.shortcuts import render, get_object_or_404, redirect
from django.core.management.base import BaseCommand
from django_project.articles.models import Article
from django_project.categories.models import Category

class Command(BaseCommand):
    help = 'Import data into MyBase'

    def handle(self, *args, **kwargs):
        articles = [
            {'title': '"How to foo?"', 'author': 'F. BarBaz', 'category_id': 1},
            {'title': '"Force 101"', 'author': 'O-W. Kenobi', 'category_id': 1},
            {'title': '"Top 10 skyscrapers"', 'author': 'K. Kong', 'category_id': 2},
            {'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla', 'category_id': 2},
            {'title': '"5 min recepies"', 'author': 'H. Lector', 'category_id': 3},
            {'title': '"my first esse"', 'author': 'sergunkit', 'category_id': 3},
        ]

        categories = [
            {'name': 'starwars', 'description': 'somewhere in a galaxy far, far away'},
            {'name': 'action', 'description': 'if it was true'},
            {'name': 'triller', 'description': 'scary histories'},
        ]

        for category in categories:
            Category.objects.create(**category)

        for article in articles:
            category_id = article.pop('category_id')
            category = get_object_or_404(Category, id=category_id)
            # category = Category.objects.get(id=category_id)
            Article.objects.create(category=category, **article)


        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
