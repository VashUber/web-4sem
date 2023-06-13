from api.models import Article
from django.db import models
from users.models import MyUser


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(MyUser, null=False, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, null=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"id: {self.id}, author: {self.author}, article: {self.article}"
