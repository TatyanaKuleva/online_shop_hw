from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Product, Category, Contact


def home(request):
    latest_products = Product.objects.all().order_by("-created_at")[:5]
    print("Последние 5 созданных продуктов:")
    print("=" * 50)
    for i, product in enumerate(latest_products, 1):
        print(f"{i}. {product.name}")
        print(f"   Цена: {product.price} руб.")
        print(f"   Создан: {product.created_at}")
        print(f"   Категория: {getattr(product.category, 'name', 'Не указана')}")
        print("-" * 30)
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"You have new message from {name}({phone}): {message}")
    contacts = Contact.objects.all()
    context = {"title": "Контакты", "contacts": contacts}
    # return render(request, 'contacts_app/contact_list.html', context)
    return render(request, "contacts.html", context)
