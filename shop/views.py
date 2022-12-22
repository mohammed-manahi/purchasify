from django.shortcuts import render, get_object_or_404
from shop.models import Product, Category


def product_list(request, category_slug=None):
    """
    Create product list view
    :param request:
    :param category_slug:
    :return: product list:
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        # Filter products based on category if it exists in the url slug
        products = Product.objects.filter(category=category)
    template = 'shop/product_list.html'
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, template, context)


def product_detail(request, id, slug):
    """
    Create product detail view
    :param request:
    :param id:
    :param slug:
    :return: product:
    """
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    template = 'shop/product_detail.html'
    context = {'product': product}
    return render(request, template, context)
