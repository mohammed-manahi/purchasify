from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from order.models import Order


@shared_task
def payment_completed(order_id):
    """
    Send invoice pdf after payment completion
    :param order_id:
    :return email:
    """
    order = Order.objects.get(id=order_id)
    subject = f'My Shop - Invoice no. {order.id}'
    message = 'Please, find attached the invoice for your recent purchase.'
    email = EmailMessage(subject, message, 'admin@purchasify.com', [order.email])
    html = render_to_string('order/pdf.html', {'order': order})
    # Use in-memory buffer for the pdf output
    out = BytesIO()
    stylesheets = [weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)
    email.attach(f'order_{order.id}.pdf',out.getvalue(), 'application/pdf')
    email.send()
