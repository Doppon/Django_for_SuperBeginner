from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

from .models import Message, Friend, Group, Good

from django.db.models import Q
from django.contrib.auth.decorators import login_required

# indexのビュー関数
@login_required(login_url='/admin/login/')
def index(request):
  #publicのuserを取得
  (public_user, public_group) = get_public()
