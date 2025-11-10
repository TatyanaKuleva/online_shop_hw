from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (ProductListView, ProductDetailView, ContactPageView, ProductCreateView, ProductUpdateView,
                           ProductDeleteView, ProductUnpublishView, ProductPublishView, ProductListByCategoryView)

app_name = CatalogConfig.name


urlpatterns = [
    path("home/", ProductListView.as_view(), name="home"),
    path("contacts/", ContactPageView.as_view(), name="contacts"),
    path("product_detail/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_detail/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product_delete/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path('product_unpublish/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='unpublish_product'),
    path('product_publish/<int:pk>/publish/', ProductPublishView.as_view(), name='publish_product'),
    path('category/<int:category_id>/products/', ProductListByCategoryView.as_view(), name='category_products'),
]
