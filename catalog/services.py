from  catalog.models import Product, Category
from django.shortcuts import get_object_or_404
from django.db.models import QuerySet

def get_products_by_category(id:int) -> tuple[Category, QuerySet[Product]]:
    category = get_object_or_404(Category, pk=id)
    products = category.products.filter()

    return category, products