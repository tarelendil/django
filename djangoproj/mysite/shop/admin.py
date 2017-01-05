from django.contrib import admin
from .models import Product, Image

class ImagesInline(admin.TabularInline):
    model = Image
    def make_dead(m, request, queryset):
        queryset.update(dead=True)


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesInline]


admin.site.register(Product, ProductAdmin)