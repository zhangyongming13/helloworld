from django.contrib import admin
from .models import Article


# 使用装饰器的方法来注册admin的定制类
@admin.register(Article)
class Article_admin(admin.ModelAdmin):
    # 定制每一个App对应的后台管理页面，list_display表示需要显示什么内容
    list_display = ('id', 'title', 'is_deleted', 'author', 'content', 'created_time', 'last_update_time')
    # ordering表示根据该值进行正序排序
    ordering = ('id',)


# Register your models here.
# admin.site.register(Article, Article_admin)  # 将刚才自己写的app的models注册到整个Django的后台管理界面
