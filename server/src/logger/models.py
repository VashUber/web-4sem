from django.db import models
from users.models import MyUser

# Create your models here.
class VisitModel(models.Model):
  user = models.CharField(default="", null=True)
  url = models.TextField(default="")
  start_at = models.DateTimeField()
  execution_time = models.TextField()
  http_user_agent = models.TextField()

  def __str__(self) -> str:
        return f"id: {self.pk}, user: {self.user}"