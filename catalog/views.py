from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseForbidden
from catalog.models import Product, Category, Contact
from catalog.services import get_products_by_category
from django.views.generic import View, ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import ProductForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.core.cache import cache


class ProductListView(ListView):
    model = Product

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        user = self.request.user
        context = self.get_context_data()
        context['can_delete_product'] = user.has_perm('catalog.delete_product')
        return self.render_to_response(context)

    def get_queryset(self):
        queryset = cache.get('product_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('product_queryset', queryset, 60 * 15)
        return queryset

class ProductListByCategoryView(ListView):
    model = Product
    template_name = 'catalog/product_list_by_category.html'
    context_object_name = 'products_by_category'

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(Category, pk=category_id)
        queryset = Product.objects.filter(category_id=category_id)
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     category_id = self.kwargs['category_id']
    #     context['category'] = get_object_or_404(Category, pk=category_id)
    #     return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs['category_id']
        category, _products = get_products_by_category(category_id)
        context['category'] = category
        context['categories'] = Category.objects.all()
        context['products'] = _products
        return context



@method_decorator(cache_page(60 * 15), name='dispatch')
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        user = self.request.user
        can_unpublish_product_perm = user.has_perm('catalog.can_unpublish_product')
        show_unpublish_button = product.is_published and can_unpublish_product_perm
        show_publish_button = not product.is_published and can_unpublish_product_perm
        context['show_unpublish_button'] = show_unpublish_button
        context['show_publish_button'] = show_publish_button
        context['can_delete_product'] = user.has_perm('catalog.delete_product')

        return context



class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_published = True
        form.instance.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            return HttpResponseForbidden("У вас нет разрешения на редактирование этого продукта.")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.is_published = True
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'
    raise_exception = True

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.owner != self.request.user:
            return HttpResponseForbidden("У вас нет разрешения на удаление этого продукта.")
        return super().dispatch(request, *args, **kwargs)

class ProductUnpublishView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'
    raise_exception = True

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = False
        product.save()
        return redirect('catalog:product_detail', pk=pk)

class ProductPublishView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'
    raise_exception = True

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.is_published = True
        product.save()
        return redirect('catalog:product_detail', pk=pk)



class ContactPageView(TemplateView):
    model = Contact
    template_name = 'catalog/contacts.html'

    def get(self, request, *args, **kwargs):

        contacts = Contact.objects.all()
        context = {"title": "Контакты", "contacts": contacts}
        return render(request, "catalog/contacts.html", context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        return HttpResponse(f"Вы получили новое сообщение от {name}({phone}): {message}")







