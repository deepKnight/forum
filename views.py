from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    block_infos = [{"name": "日常专区", "desc": "一个栗子", "manager": "admin"},
                   {"name": "战术交流", "desc": "一个栗子", "manager": "admin"},
                   {"name": "论坛建设", "desc": "一个栗子", "manager": "admin"},]
    return render(request, "index.html", {"blocks":block_infos})
