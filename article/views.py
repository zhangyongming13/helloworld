# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from .models import Article
# Create your views here.


# article_id是由urls.py路径中传入的，表示数据库中的主键
def article(request, article_id):
    # try:
        #  利用object.get的方法获取到对应article_id主键的内容包括title和content
        # article = Article.objects.get(id=article_id)  # article式Article的对象，含有title和content等内容
    article = get_object_or_404(Article, pk=article_id)  # 获取对应主键的数据库数据
    context = {}  # 传入html的数据式dict字典类型
    context['article_dict'] = article
    return render_to_response('article_detail.html', context)
        # return render(request, 'article_detail.html', context)  # render表示使用mhtml模板
    # except Article.DoesNotExist:
    #     raise Http404('not found!')
        # return HttpResponse('<h2>DoesNotExist this page!!!</h2>')
    # return HttpResponse('<h2>article title is %s </h2><br>content is %s' % (article.title, article.content))


def article_list(request):
    # 利用objects.all获取对象所有元素，上面的式根据article_id获取对应新闻的属性
    # 利用objects.filter来过滤相应的内容，下面的表示只有is_delete=False才去获取
    get_article_list = Article.objects.filter(is_deleted=False)
    context = {}
    context['article_list'] = get_article_list
    # 使用相应的模板
    return render_to_response('article_list.html', context)
