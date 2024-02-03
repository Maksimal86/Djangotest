from django.contrib import admin
from .models import News, Category



class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'created_at', 'update_at', 'is_published') # какие поля хотим видеть в админке
    list_display_links = ('id', 'title') # обзначаем поля, которые будут ссылками
    search_fields = ('title', 'created_at', 'update_at', 'content') # поля, по которым может осущестляться поиск
    list_editable = ('is_published',) # поля, которые можно редактировать из админки
    list_filter = ('is_published','category') # по каким полям фильтровать



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title') # какие поля хотим видеть в админке
    list_display_links = ('id', 'title') # обзначаем поля, которые будут ссылками
    search_fields = ('title',) # поля, по которым может осущестляться поиск

admin.site.register(News, NewsAdmin) # порядок важен
admin.site.register(Category, CategoryAdmin)