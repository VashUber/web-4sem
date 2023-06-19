from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from .models import MyUser


@shared_task
def sendEmailVerification(data):
    send_mail(
        subject="Верификация",
        from_email=None,
        message=data["body"],
        recipient_list=data["email_to"],
    )


@shared_task
def SendRegisterUserToAdmin():
    start_date = datetime.today() - timedelta(days=1)
    end_date = start_date + timedelta(days=1)
    users = MyUser.objects.all().filter(created_ad__range=[start_date, end_date])
    content = f"Новые пользователи за сегодня: {str(len(users))}\n"
    for user in users:
        content += f"id: {str(user.id)}, email: {str(user.email)}\n"

    send_mail(
        subject="Пользователи",
        message=content,
        from_email=None,
        recipient_list=["admin@test.com"],
    )
