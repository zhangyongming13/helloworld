from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)  # 新闻的标题使用CharField字段，限制最大长度
    content = models.TextField()  # 文章使用TextField字段
    # 自动添加创建时间
    # created_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    # 利用django自带的用户认证模型为新闻添加作者，on_delete表示文章删除的时候对关联对应的作者的操作，这里式不做任何操作
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    # is_delete表示是否逻辑删除，一般情况下不会真的删除数据库中的文件，要一篇文件不显示可以讲
    # 该值改为True再到views.py文件中利用过滤器进行过滤
    is_deleted = models.BooleanField(default=False)
    readed_num = models.IntegerField(default=0)

    def __str__(self):
        # 返回title名，后台显示title
        return '<article: %s>' % self.title
