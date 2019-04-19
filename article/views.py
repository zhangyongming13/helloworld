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
