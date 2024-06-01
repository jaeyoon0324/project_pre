from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, default='http://example.com')  # 기본값 제공
    image_url = models.URLField(max_length=200, null=True, blank=True)  # 새로운 필드 추가
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
