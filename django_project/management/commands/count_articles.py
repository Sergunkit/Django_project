from django.core.management.base import BaseCommand
from django_project.articles.models import Article

class Command(BaseCommand):
    help = 'Count articles in the database'

    def handle(self, *args, **kwargs):
        count = Article.objects.count()
        self.stdout.write(str(count))
