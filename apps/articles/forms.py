from django import forms
from .models import *


class articleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            "title",
            "content",
        )
        labels = {
            "title": "제목",
            "content": "내용",
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        labels = {
            "content": "댓글",
        }
