from django.contrib import admin
from shop.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ['id', 'name', 'price', 'is_popular']  # Добавлено поле 'is_popular'
    list_editable = ['name', 'price', 'is_popular']  # Поле 'is_popular' теперь можно редактировать в списке

    def get_queryset(self, request):
        """
        Функция для оптимизации запроса к базе данных, включая предварительную выборку
        всех необходимых данных, чтобы уменьшить количество запросов при отображении списка.
        """
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('category')  # Пример использования prefetch_related для связанных данных
        return queryset
