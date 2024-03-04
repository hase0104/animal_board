from django import forms
from .models import Category, Message, Comment, Good
from django.contrib.auth.models import User


class TitleForm(forms.ModelForm):
    title = forms.CharField(max_length=100)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
        widgets={
            "content":forms.Textarea(attrs={"class":"form-control form-control-sm", "rows":2}),
        }