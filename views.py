from django.http import HttpResponse
from django.shortcuts import render
from block.models import Block

def index(request):
    # block_infos = [{"name": "日常专区", "desc": "一个栗子", "manager": "admin"},
    #                {"name": "战术交流", "desc": "一个栗子", "manager": "admin"},
    #                {"name": "论坛建设", "desc": "一个栗子", "manager": "admin"},]
    block_infos = Block.objects.all().order_by("id")
    return render(request, "index.html", {"blocks":block_infos})
