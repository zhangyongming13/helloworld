from django.http import HttpResponse


def index(request):  # request参数式固定的
    return HttpResponse('Hello world!是多少')  # 利用HttpResponse返回响应的内容
