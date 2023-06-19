from celery import shared_task
from dateutil import parser
from django.core.mail import send_mail
from users.models import MyUser

from .models import Article


@shared_task
def SendCommentOnArticle(data):
    article = Article.objects.get(pk=data["article"])
    author_comment = MyUser.objects.get(pk=data["author"])
    content = f'На ваш пост "{article.title}" написан новый комментарий. \n'
    content += f"Почта автора: {author_comment.email} \n"
    content += f"Комментарий: {data['text']} \n"
    date_format = parser.isoparser().isoparse(data["created_at"]).strftime("%d.%m.%Y %H:%M:%S")
    content += f"Дата создания: {date_format} \n"
    send_mail(subject="Новый комментарий", message=content, from_email=None, recipient_list=[article.author.email])
