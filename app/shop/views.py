from django.shortcuts import render
from .models import Product
from django.views.generic import ListView, DetailView

# Главная страница
def index(request):
    # Получаем популярные продукты
    popular_products = Product.objects.filter(is_popular=True).order_by('-price')[:4]

    # Разделяем описание каждого продукта на строки
    for product in popular_products:
        product.description_lines = product.description.split('\n')

    return render(request, 'shop/index.html', {'popular_products': popular_products})
# Список продуктов
class ProductListView(ListView):
    model = Product
    template_name = 'shop/product_list.html'  # Убедитесь, что путь правильный
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

    def get_context_data(self, **kwargs):
        # Добавляем в контекст обработанные данные
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            # Разбиваем описание на список строк
            product.description_list = product.description.split(',') if product.description else []
        return context
# Детальная информация о продукте
class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_detail.html'  # Убедитесь, что путь правильный
    context_object_name = 'product'
