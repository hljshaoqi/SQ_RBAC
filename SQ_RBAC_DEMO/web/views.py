import json
from datetime import datetime

from django.shortcuts import render, HttpResponse, redirect

from web import models
from rbac.service import initial_permission


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        u = request.POST.get('username')
        p = request.POST.get('password')
        obj = models.UserInfo.objects.filter(user__username=u, user__password=p).first()
        if obj:
            request.session['user_info'] = {'username': u, 'nickname': obj.nickname, 'nid': obj.id}
            initial_permission(request, obj.user_id)
            return redirect('/index.html')
        else:
            return render(request, 'login.html')


def index(request):
    if not request.session.get('user_info'):
        return redirect('/login.html')

    return HttpResponse('ok')
