from django.db import models
from users.models import User

class Chat(models.Model):
    question = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    answer = models.TextField(null=True, blank=True)