from django.views.generic.base import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


def about(request):
    return render(request, 'about.html')


def articles(request):
    return render(
        request,
        'templates.articles.index.html',
        )

def categories(request):
    return render(
        request,
        'templates.categories.index.html',
        )
