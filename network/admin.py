from django.contrib import admin
from network.models import NetworkNode, Product
from django.utils.html import format_html
from django.contrib import admin


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'supplier_link', 'debt', 'level')
    list_filter = ('city',)
    actions = ['clear_debt']

    def supplier_link(self, obj):
        if obj.supplier:
            link_url = f'http://127.0.0.1:8000/network/nodes/{obj.supplier.id}/'
            return format_html('<a href="{}">{}</a>',link_url, obj.supplier.name)
        else:
            return "-"
    supplier_link.short_description = "Поставщик"

    @admin.action(description='Очистить задолженность для выбранных узлов')
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, "Задолженность очищена.")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date', 'network_node')
