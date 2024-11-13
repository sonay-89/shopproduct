from shopproduct.celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_regular_email():
    send_mail(
        "Плановое письмо",
        "Это плановое сообщение.",
        "отправитель@gmail.com",
        ["получатель@example.com"],
        fail_silently=False,
    )
