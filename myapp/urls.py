from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/new/', views.article_create, name='article_create'),
    path('articles/<int:pk>/', views.article_detail, name='article_detail'),
    path('articles/<int:pk>/edit/', views.article_edit, name='article_edit'),
    path('articles/<int:pk>/delete/', views.article_delete, name='article_delete'),
    path('articles/<int:pk>/ajax/', views.article_detail_ajax, name='article_detail_ajax'),
    path('category/<int:category_id>/', views.articles_by_category, name='category_articles'),
    path('bookmarks/', views.bookmarked_articles, name='bookmarked_articles'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),





]
