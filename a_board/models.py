from django.db import models
from django.contrib.auth.models import User

# Category
class Category(models.Model):
    category = models.TextField(max_length=100)


# Message
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_owner")
    content = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    good_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="message_category")

# Comment
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_owner")
    message = models.ForeignKey(Message, owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_owner"))
    pub_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=500)


# Good
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="good_owner")
    good_message = models.ForeignKey(Message, owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="good_message_owner"))
    pub_date = models.DateTimeField(auto_now_add=True)



# Create your models here.
