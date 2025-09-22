# from django import forms


# class ArticleForm(forms.Form):
#     content = forms.CharField(label="Комментарий", max_length=200)


from django.forms import ModelForm
from .models import Article


class ArticleCreateForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "author", "category"]
