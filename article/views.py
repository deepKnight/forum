from django.http import HttpResponse
from django.shortcuts import render,redirect
from article.models import Article
from block.models import Block
from article.forms import ActicleForm


def article_list(request, block_id):
    block_id = int(block_id)
    block = Block.objects.get(id=block_id)
    articles_objs = Article.objects.filter(block=block, status=0).order_by("-id")
    return render(request, "article_list.html", {"articles": articles_objs, "b": block})


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
