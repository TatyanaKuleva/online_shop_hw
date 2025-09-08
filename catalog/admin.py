from django.contrib import admin
from catalog.models import Product, Category, Contact
from django.utils.html import format_html


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category", "images")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px;"/>', obj.image.url)
        return ''

    image_tag.short_description = 'Изображение продукта'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = (
        "name",
        "description",
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "address")
    search_fields = (
        "name",
        "email",
        "phone",
    )
