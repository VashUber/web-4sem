from django.db import models
from users.models import MyUser


class Article(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    content_text = models.TextField()
    count_reads = models.IntegerField(default=0)
    img = models.ImageField(upload_to="articlePreview", blank=True, null=True)

    def __str__(self) -> str:
        return f"id: {self.id}, title: {self.title}"
