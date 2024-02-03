from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category


def news(request):
    new = News.objects.order_by('-created_at') #сортировка здесь
    new = News.objects.all() #сортировка черз models
    categories = Category.objects.all()
    return render(request, 'news/newsnews.html',{'news': new, 'title': 'список новостей', 'categories':categories})


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(id=category_id)
    return render(request, 'news/category.html', {'news': news, 'categories': categories, 'category':category})

def test(request):
    return HttpResponse('<h1>Тестовая страница</h1>')