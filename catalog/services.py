from  catalog.models import Product, Category


def get_products_by_category(category_id):
    category = Category.objects.filter(pk=category_id).first()
    products = Product.objects.filter(category=category)
    return products

