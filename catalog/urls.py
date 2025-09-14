from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ContactPageView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView)

app_name = CatalogConfig.name


urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_detail/<int:pk>/update", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/delete", ProductDeleteView.as_view(), name="product_delete"),
]
