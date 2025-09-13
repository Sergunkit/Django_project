from django.test import TestCase
from django.urls import reverse


class CategoriesTest(TestCase):
    def test_categories_list(self):
        response = self.client.get(reverse("categories_index"))
        self.assertEqual(response.status_code, 200)

    # Проверяем наличие данных в контексте шаблона
        self.assertIn("categories", response.context)
        categories = response.context["categories"]

    # Проверяем не пустой ли список
        self.assertTrue(len(categories) > 0)
