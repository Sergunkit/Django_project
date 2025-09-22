from django import forms
from django_project.categories.models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(max_length=200, required=True)

    class Meta:
        model = Category
        fields = ['name', 'description']
