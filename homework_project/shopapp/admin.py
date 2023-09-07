from django.contrib import admin
from .models import User, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'price', 'amount']
    ordering = ['-amount', 'name']
    list_filter = ['add_date', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    """Отдельный продукт."""
    readonly_fields = ['add_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Категория товара и его подробное описание',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'amount'],
            }
        ),
        (
            'Прочее',
            {
                'fields': ['add_date'],
            }
        ),
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'lastname', 'email']
    ordering = ['lastname', 'name']
    list_filter = ['registration']
    search_fields = ['name', 'lastname', 'email']
    search_help_text = 'Поиск имени и email'

    readonly_fields = ['registration']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'lastname'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробная информация о клиенте',
                'fields': ['email', 'phone', 'address'],
            },
        ),
        (
            'Прочее',
            {
                'fields': ['registration'],
            }
        ),
    ]


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    ordering = ['-total_price', 'customer']
    list_filter = ['date_ordered', 'total_price']

    readonly_fields = ['date_ordered', 'total_price']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer', 'date_ordered'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробности заказа',
                'fields': ['products'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['total_price'],
            }
        ),
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
