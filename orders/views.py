from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .models import OrderItem
from .forms import OrderCreateForm
from cafe.models import CustomUser
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import *
from .forms import *
from .models import Order
from cafe.models import *
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string
# import weasyprint
from .tasks import order_created


@staff_member_required
def admin_order_pdf(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    html = render_to_string('orders/order/pdf.html',
                            {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=\
        "order_{}.pdf"'.format(order.id)
    # weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')])
    return response


@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'admin/orders/order/detail.html',
                  {'order': order})


@login_required
def order_create(request):
    cart = Cart(request)
    order=Order(username=request.user)
    #order = Order(username=request.user, first_name=CustomUser.first_name, last_name=CustomUser.last_name, email=CustomUser.email, address=CustomUser.address, postal_code=CustomUser.zipcode, city=CustomUser.city)
    if request.method == 'POST':

        form = OrderCreateForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            #            order.username = CustomUser.username
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            # order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
        return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm(instance=order)
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


@login_required
def order_list(request, username_id):
    order = None
    orders = Order.objects.all()
    if username_id:
        orders = Order.objects.filter(username_id=username_id)
        return render(request,
                      'orderlist.html',
                      {'orders': orders,
                       'order': order})


@login_required
def order_detail(request, username_id, order_id):
    order = None
    if order_id:
        order = get_object_or_404(Order, id=order_id)
    return render(request,
                  'order_item.html',
                  {'order': order})
