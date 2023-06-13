from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display = ('created_ad', 'author', 'title', 'content', 'content_text', 'img', 'id')

admin.site.register(Article, ArticleAdmin)
