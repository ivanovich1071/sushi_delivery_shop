from django.urls import path
from .views import index, ProductListView, ProductDetailView

app_name = 'shop'  # Добавляем пространство имен

urlpatterns = [
    path('', index, name='index'),  # Главная страница
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
