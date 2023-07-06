from django.db import models

from members.models import CustomUser


class Board(models.Model):
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(default="")
    date = models.DateTimeField(auto_now_add=True)
    isAnonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Board, null=False, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    isAnonymous = models.BooleanField(default=False)

    def __str__(self):
        return self.post