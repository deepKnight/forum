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
        #     article = Article(block=block, title=form.clean_data["title"],
        #                       content=form.changed_data["content"], status=0)
        #     article.save()
            return  redirect("/article/list/%s" % block_id)
        else:
            return render(request, "article_create.html", {"b": block, "error": "标题和内容都不能为空。","form":form})
                                                           #  "title": request.POST["title"],
                                                           # "content": request.POST["content"]})
        # title = request.POST["title"]
        # content = request.POST["content"]
        # if not title or not content:
        #     return render(request, "article_create.html", {"b": block, "error": "标题和内容都不能为空。",
        #                                                    "title": title, "content": content})
        # if len(title)>100 or len(content)>10000:
        #     return render(request, "article_create.html", {"b": block,
        #                                                    "error": "标题不能超过100字/n内容不能超过10000字",
        #                                                    "title": title, "content": content})
        # article = Article(block=block, title=title, content=content, status=0)
        # article.save()
        # return redirect("/article/list/%s" % block_id)
