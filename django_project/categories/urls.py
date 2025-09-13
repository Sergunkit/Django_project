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
        path('<int:id>/', views.Categories_view.as_view(), name='categories_detail'),
]

