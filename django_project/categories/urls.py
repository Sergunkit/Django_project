from django.urls import path
from django_project.categories import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path("about/", views.about),
#     path("articles/", include("django_project.articles.urls")),
#     path('', views.base),
# ]

urlpatterns = [
        path('', views.Index.as_view(), name='categories_index'),
        path('<int:id>/update/', views.Category_update.as_view(), name='category_update'),
        path('<int:id>/delete/', views.Category_delete.as_view(), name="category_delete"),
        path('<int:id>/', views.Category_view.as_view(), name='category_detail'),
        path('create/', views.CategoryFormView.as_view(), name='category_create'),
]


