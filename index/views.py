from django.shortcuts import render

# 首页
def indexView(request):
    username=request.user.username
    return render(request,'index.html',locals())