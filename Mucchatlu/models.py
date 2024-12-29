from django.db import models
from django.utils.timezone import now

class Thread(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title

class Message(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    nickname = models.CharField(max_length=50)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nickname}: {self.content[:30]}"
