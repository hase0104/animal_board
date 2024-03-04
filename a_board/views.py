from django.shortcuts import render
from django.shortcuts import redirect

from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Category, Message, Comment, Good
from .forms import MessageForm


# indexのビュー関数
def index(request, page=1):
    max = 10
    msgs = Message.objects.all()
    paginate = Paginator(msgs, max)
    page_items = paginate.get_page(page)

    params = {
        "login_user":request.user, #ログインしてない人の表示は？
        "content":page_items,
    }
    return render(request, 'index.html', params)

# postのビュー
@login_required(login_url="user_login")
def post(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        content = request.POST["content"]
        msg = Message()
        msg.owner = request.user
        msg.content = content
        msg.save()
        return redirect(to="/index/") #確認

    else:
        messages = Message.objects.filter(owner=request.user)
        params ={
            "login_user":request.user,
            "content":messages,
        }
        return render(request, "index.html", params) #確認

# post_list
def post_list(request, page=1):
    max = 10


#login
def user_login(request,):



#good
def good(request, good_id):

#edit

#create_user

#comment


# Create your views here.
