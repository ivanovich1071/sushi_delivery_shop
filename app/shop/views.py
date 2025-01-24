from django.shortcuts import render
from shop.models import Product

def index(request):
    # Получаем популярные товары, отсортированные по убыванию цены
    popular_products = Product.objects.filter(is_popular=True).order_by('-price')[:4]  # Отображаем только 4 товара
    context = {
        'title': 'Доставка суши SusiShop',
        'popular_products': popular_products,  # Добавляем популярные товары в контекст
    }
    return render(request, 'index.html', context)

from django.views.generic import ListView, DetailView

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        sort_option = self.request.GET.get('sort')
        if sort_option == 'asc':
            queryset = queryset.order_by('price')
        elif sort_option == 'desc':
            queryset = queryset.order_by('-price')
        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
