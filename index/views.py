from django.shortcuts import render,redirect
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from index import models
# 首页
def indexView(request):
    username=request.user.username
    return render(request,'index.html',locals())

#查询用户信息
def userInfo_list(request):
    #查询所有数据
    ret = models.UserInfo.objects.all()
    for i in ret:
        print(i.id,i.name)
    # return HttpResponse("查询成功！")
    return render(request,'userInfo.html',{"user_list": ret})

#添加数据
@csrf_exempt
def add_user(request):
    if request.method == "POST":
        new_name = request.POST.get("username",'');
        models.UserInfo.objects.create(name = new_name);
        return redirect("/userInfo");
        # return HttpResponse("新增数据成功！")
    # return render(request, 'add_user.html',locals())
    else:
        print("进来了")
        return render(request,'add_user.html')