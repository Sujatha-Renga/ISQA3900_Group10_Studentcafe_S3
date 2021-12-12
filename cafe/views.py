from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.urls import reverse
from cart.forms import CartAddProductForm
from django.core.mail import EmailMessage
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm



# Create your views here.
def home(request):
    return render(request, 'cafe/home.html',
                  {'cafe': home})



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'cafe/home.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def menu_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'cafe/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'cafe/product/detail.html', context)


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
