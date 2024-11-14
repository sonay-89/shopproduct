from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_regular_email():
    send_mail(
        "Плановое письмо",
        "Это плановое сообщение.",
        "aloy02102024@gmail.com",
        ["aloy02102024@gmail.com"],
        fail_silently=False,
    )
