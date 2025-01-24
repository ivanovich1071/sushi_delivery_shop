from django.shortcuts import render
from shop.models import Product

def index(request):
    popular_products = Product.objects.filter(is_popular=True).order_by('-price')[:4]
    for product in popular_products:
        product.description_lines = product.description.split('\n')  # Разбиваем описание на строки
    context = {
        'popular_products': popular_products,
    }
    return render(request, 'shop/index.html', context)
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
