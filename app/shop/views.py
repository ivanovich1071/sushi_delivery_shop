from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView

# Главная страница
def index(request):
    # Получаем список популярных продуктов, отсортированных по убыванию цены
    popular_products = Product.objects.filter(is_popular=True).order_by('-price')[:4]
    for product in popular_products:
        # Разбиваем описание на строки для отображения списком
        product.description_lines = product.description.split(' - ')  # Исправлено
    context = {
        'popular_products': popular_products,
    }
    return render(request, 'shop/index.html', context)

# Список продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'  # Убедитесь, что здесь указан правильный путь
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        # Сортировка продуктов по параметру sort
        sort_option = self.request.GET.get('sort')
        if sort_option == 'asc':
            queryset = queryset.order_by('price')
        elif sort_option == 'desc':
            queryset = queryset.order_by('-price')
        return queryset

# Детальная информация о продукте
class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'  # Убедитесь, что путь правильный
    context_object_name = 'product'
