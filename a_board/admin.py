from django.contrib import admin
from .models import Message, Comment, Category, Good

admin.site.register([Message, Comment, Category, Good])


#以下うまく動いてたら消す
# admin.site.register(Message)
# admin.site.register(Comment)
# admin.site.register(Category)
# admin.site.register(Good)


# Register your models here.
