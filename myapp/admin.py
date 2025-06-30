from django.contrib import admin
from .models import NewsArticle, Category
# Register your models here.

admin.site.register(NewsArticle)
admin.site.register(Category)