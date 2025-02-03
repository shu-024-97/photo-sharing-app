from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username

class Photo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # アップロードしたユーザー
    image = models.ImageField(upload_to='photos/')  # 画像ファイル
    caption = models.TextField(blank=True)  # キャプション（任意）
    created_at = models.DateTimeField(auto_now_add=True)  # アップロード日時

    def __str__(self):
        return f"{self.user.username} - {self.image.name}"