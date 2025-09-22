from django.test import TestCase
from django.urls import reverse
from .models import Article
from django_project.categories.models import Category


class ArticlesTest(TestCase):
    

    def test_articles_list(self):
        response = self.client.get(reverse("articles_index"))
        self.assertEqual(response.status_code, 200)


        # Проверяем наличие данных в контексте шаблона
        self.assertIn("articles", response.context)
        articles = response.context["articles"]

        # Проверяем не пустой ли список статей
        self.assertTrue(len(articles) > 0)


    def setUp(self):
        self.category = Category.objects.create(name='some category', description='some description')
        self.article = Article.objects.create(
            title="some article",
            author="john example",
            category=self.category,
        )


    def test_article_update_flow(self):
        update_url = reverse("article_update", kwargs={"id": self.article.id})
        list_url = reverse("articles_index")

        # Отправка POST-запроса на изменение
        self.client.post(update_url, data={
            "title": "some Bob",
            "author": self.article.author,
            "category": self.category.id,
        })

        # Переход на страницу списка статей
        response = self.client.get(list_url)

        # Проверяем, что новое название отрисовано в HTML
        self.assertContains(response, "some Bob")
        self.assertNotContains(response, "some article")

    # как вариант можно не создавать новую запись для проверки, а использовать фикстуры:
    # fixtures = ["articles.json"] # (переменная класса)
    # потом берем запись по pk и меняем данные:
    # update_url = reverse("articles:update", kwargs={"pk": 1})
    # self.client.post(update_url, data={"name": "Bob"})
    # и потом так же проверяем полученный список
