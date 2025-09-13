from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter


# файл для админ панели
# class ArticleAdmin(admin.ModelAdmin):
#     search_fields = ["title", "author"]
# admin.site.register(Article, ArticleAdmin)


@admin.register(Article) # позволяет связать модель с классом и провести регистрацию...
# ...модели в разделе администратора (без admin.site.register(Article))
class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        # "created_at",
    )  # Перечисляем поля, отображаемые в таблице списка статей
    search_fields = ["title", "author"] # По этим полям будет осуществляться поиск.
    # list_filter = (
    #     ("created_at", DateFieldListFilter),
    # )  # Перечисляем поля для фильтрации
