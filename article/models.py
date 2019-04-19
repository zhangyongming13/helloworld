from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)  # 新闻的标题使用CharField字段，限制最大长度
    content = models.TextField()  # 文章使用TextField字段
