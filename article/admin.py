from django.contrib import admin
from .models import Article

# Register your models here.
admin.site.register(Article)  # 将刚才自己写的app的models注册到整个Django的后台管理界面
