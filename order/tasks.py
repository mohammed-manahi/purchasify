from celery import shared_task
from django.core.mail import send_mail
from order.models import Order


@shared_task
def order_created(order_id):
    """
    Utilize celery background worker to send email when order is created
    :param order_id:
    :return mail:
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order no. {order.id}'
    message = f'Dear {order.first_name},\n\n' \
              f'You have successfully placed an order.' \
              f'Your order ID is {order.id}.'
    mail_sent = send_mail(subject, message, 'admin@purchasify.com', [order.email])
    return mail_sent
