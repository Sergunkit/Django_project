from django.db import models
from django_project.categories.models import Category

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True) PROTECT не позволяет удалять категории
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# class ArticleComment(models.Model):
#     content = models.CharField("content", max_length=100)

# STATUS_CHOICES = [('TR', 'Trainee'), ('JR', 'Junior'), ('SR', 'Senior'), ('CEO', 'CEO')]

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     position = models.CharField(max_length=3, choices=STATUS_CHOICES, default='TR')

