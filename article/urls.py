from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_id>', views.article, name = 'article_detail'),
    path('article_list/', views.article_list, name = 'article_list'),
]
