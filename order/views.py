from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse
from cart.cart import Cart
from order.models import Order, OrderItem
from order.forms import OrderCreateForm
from order.tasks import order_created


def order_create(request):
    """
    Create a view for order create
    :param request:
    :return order:
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(data=request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            # Add celery background task for sending email after an order is created
            order_created.delay(order.id)
            # Get the order if rom the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
        template = 'order/order_create.html'
        context = {'cart': cart, 'form': form}
        return render(request, template, context)


@staff_member_required
def admin_order_detail(request, order_id):
    """
    Create custom view in admin site for order details
    :param request:
    :param order_id:
    :return order detail:
    """
    order = get_object_or_404(Order, id=order_id)
    template = 'admin/order/detail.html'
    context = {'order': order}
    return render(request, template, context)
