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

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_welcome_email(user_email, username):
    """
    Отправка приветственного письма новому пользователю.
    """
    subject = "Добро пожаловать!"
    message = f"Привет, {username}! Спасибо за регистрацию на нашем сайте."
    from_email = "noreply@yourdomain.com"
    recipient_list = [user_email]

    send_mail(subject, message, from_email, recipient_list)