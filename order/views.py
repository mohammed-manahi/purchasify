from django.shortcuts import render
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
            template = 'order/order_created.html'
            context = {'order': order}
            return render(request, template, context)
    else:
        form = OrderCreateForm()
        template = 'order/order_create.html'
        context = {'cart': cart, 'form': form}
        return render(request, template, context)
