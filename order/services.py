from django.core.mail import send_mail

from config import settings


def send_order_email(order_item):
    send_mail(
        'Заявка на покупку лодки ',
        f'{order_item.name} ({order_item.email}) хочет купить лодку {order_item.boat.name}. Вот сообщение: {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.boat.owner.email],
    )
