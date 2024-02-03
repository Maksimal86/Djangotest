from django.urls import path

from .views import *

urlpatterns = [
    path('', news, name='home' ),      # 'news/' откинули в firstsite.urls
    path('test/', test ),
    path('cat/<int:category_id>/', get_category, name='category'),
]