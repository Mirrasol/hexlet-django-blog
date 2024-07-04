from django.urls import path
from hexlet_django_blog.article.views import IndexView, ArticleView, index

urlpatterns = [
    path('', IndexView.as_view()),
    path('<int:id>/', ArticleView.as_view(), name='article_show'),
    path('<str:tags>/<int:article_id>/', index, name='article')
]
