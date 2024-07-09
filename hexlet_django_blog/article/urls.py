from django.urls import path
from hexlet_django_blog.article.views import (
    IndexView,
    ArticleView,
    ArticleFormCreateView,
    ArticleFormUpdateView,
    ArticleFormDeleteView,
    index,
)

urlpatterns = [
    path('', IndexView.as_view(), name='articles_index'),
    path('create/', ArticleFormCreateView.as_view(), name='article_create'),
    path('<int:id>/update/', ArticleFormUpdateView.as_view(), name='article_update'),
    path('<int:id>/delete/', ArticleFormDeleteView.as_view(), name='article_delete'),
    path('<int:id>/', ArticleView.as_view(), name='article_show'),
    path('<str:tags>/<int:article_id>/', index, name='article'),
]
