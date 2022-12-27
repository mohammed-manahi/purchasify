import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import Order


@csrf_exempt
def stripe_webhook(request):
    """
    Utilize stripe webhooks
    :param request:
    :return:
    """
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(payload, signature_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError as error:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as error:
        # Invalid signature
        return HttpResponse(status=400)
    if event.type == 'checkout.session.completed':
        session = event.data.object
        if session.mode == 'payment' and session.payment_status == 'paid':
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
            # Mark order as paid
            order.paid = True
            order.save()
    return HttpResponse(status=200)
