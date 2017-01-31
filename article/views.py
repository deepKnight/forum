from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from article.models import Article
from block.models import Block
from article.forms import ActicleForm
ARTICLE_CNT_1PAGE = 15

def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    page_no = int(request.GET.get("page_no", "1"))
    all_articles = Article.objects.filter(block=block, status=0).order_by("-id")
    p = Paginator(all_articles, ARTICLE_CNT_1PAGE)
    page = p.page(page_no)
    articles_objs = page.object_list
    return render(request, "article_list.html", {"articles": articles_objs, "b": block, "paginator": p, "page": page})


def article_create(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    if request.method == "GET":
        return render(request, "article_create.html", {"b": block})
    else:
        form = ActicleForm(request.POST)
        if form.is_valid():
            acticle = form.save(commit=False)
            acticle.block = block
            acticle.status = 0
            acticle.save()
            return  redirect("/article/list/%s" % block_id)
        else:
            return render(request, "article_create.html", {"b": block, "error": "标题和内容都不能为空。","form":form})

def article_detail(request, aid):
    article = Article.objects.get(id=aid)
    return render(request, "article_detail.html", {"a": article})
