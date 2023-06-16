from datetime import datetime, timedelta

from celery import shared_task
from django.core.mail import send_mail

from .models import Article


@shared_task
def SendNewArticleToAdmin():
    start_date = datetime.today() - timedelta(days=1)
    end_date = start_date + timedelta(days=1)
    users = Article.objects.all().filter(created_ad__range=[start_date, end_date])
    content = "Новые посты за сегодня: \n"
    for user in users:
        content += f"{str(user.title)}\n"

    send_mail(
        subject="Посты",
        message=content,
        from_email=None,
        recipient_list=["admin@test.com"],
    )


@shared_task
def CountsReads():
    start_date = datetime.today() - timedelta(days=1)
    end_date = start_date + timedelta(days=1)
    articles = Article.objects.all().filter(created_ad__range=[start_date, end_date])
    counts = {}
    for article in articles:
        if str(article.author.email) in counts:
            counts[str(article.author.email)] += article.count_reads
        else:
            counts[str(article.author.email)] = article.count_reads

    for key, value in counts.items():
        content = f"Статистика просмотров ваших постов: {str(value)}"
        send_mail(
            subject="Статистика просмотров",
            message=content,
            from_email=None,
            recipient_list=[key],
        )

    return counts
