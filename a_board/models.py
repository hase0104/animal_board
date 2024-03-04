from django.db import models
from django.contrib.auth.models import User

# Category
class Category(models.Model):
    category = models.TextField(max_length=100)

    def __str__(self):
        return f"{str(self.category)}"

# Message
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_owner")
    content = models.TextField(max_length=1000)
    title = models.CharField(max_length=100)
    good_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="message_category")
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{str(self.title)} {str(self.content)} (Owner:{self.owner})"

    class Meta:
        ordering = ("-pub_date",)


# Comment
class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_owner")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="comment_message")
    pub_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(max_length=500)

    def __str__(self):
        return f"{str(self.message)} (Owner:{self.owner})"

    class Meta:
        ordering = ("-pub_date",)


# Good
class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="good_owner")
    good_message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="goods")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.good_message)} (Owner:{self.owner})"

    class Meta:
        ordering = ("-pub_date",)


# Create your models here.
