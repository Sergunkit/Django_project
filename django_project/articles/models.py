from django.db import models
from django_project.categories.models import Category

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)


    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# STATUS_CHOICES = [('TR', 'Trainee'), ('JR', 'Junior'), ('SR', 'Senior'), ('CEO', 'CEO')]

# class Employee(models.Model):
#     name = models.CharField(max_length=255)
#     position = models.CharField(max_length=3, choices=STATUS_CHOICES, default='TR')



# Мы осуществляем связь статей с категориями. Следующий шаг - добавить в данные статей отсылку на категории.
# Нужно данным придать какой-то смысл для наглядности
# Затем нужно принять articles в шаблоне категории и сделать отображение статей относящихся к конкретной категории
# В статье нужно отобразить категорию как ссылку с переходом отображения категории
