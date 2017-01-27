from django import forms
from article.models import Article

# class ActicleForm(forms.Form):
#     title = forms.CharField(label="标题",max_length=100)
#     content = forms.CharField(label="内容",max_length=10000)

class ActicleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']