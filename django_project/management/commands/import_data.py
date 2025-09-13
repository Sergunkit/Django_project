from django.core.management.base import BaseCommand
from django_project.articles.models import Article

class Command(BaseCommand):
    help = 'Import data into MyBase'

    def handle(self, *args, **kwargs):
        articles = [
            {'title': '"How to foo?"', 'author': 'F. BarBaz', 'category': '1'},
            {'title': '"Force 101"', 'author': 'O-W. Kenobi', 'category': '1'},
            {'title': '"Top 10 skyscrapers"', 'author': 'K. Kong', 'category': '2'},
            {'title': '"Top 10 skyscrapers (jp. edition)"', 'author': 'K. Godzilla', 'category': '2'},
            {'title': '"5 min recepies"', 'author': 'H. Lector', 'category': '3'},
        ]

        for item in articles:
            Article.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))
