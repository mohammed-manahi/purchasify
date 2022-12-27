import stripe
from decimal import Decimal
from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.conf import settings
from order.models import Order

# Create stripe api instance
stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def payment_process(request):
    """
    Create payment process view
    :param request:
    :return payment checkout:
    """
    order_id = request.session.get('order_id', None)
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        success_url = request.build_absolute_uri(reverse('payment:completed'))
        cancel_url = request.build_absolute_uri(reverse('payment:canceled'))
        # Stripe checkout data
        session_data = {'mode': 'payment', 'client_reference_id': order_id, 'success_url': success_url,
                        'cancel_url': cancel_url, 'line_items': []}
        # Append order details to the line items in stripe data
        for item in order.items.all():
            session_data['line_items'].append({
                'price_data': {
                    # Unit amount in cents
                    'unit_amount': int(item.price * Decimal('100')),
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                    },
                },
                'quantity': item.quantity,
            })
        session = stripe.checkout.Session.create(**session_data)
        return redirect(session.url, code=303)
    else:
        # locals() returns the variables defined in the view to the template
        template = 'payment/process.html'
        return render(request, template, locals())


def payment_completed(request):
    """
    Create payment success view
    :param request:
    :return payment success:
    """
    template = 'payment/completed.html'
    return render(request, template)


def payment_canceled(request):
    """
    Create payment cancel view
    :param request:
    :return payment cancel:
    """
    template = 'payment/canceled.html'
    return render(request, template)
