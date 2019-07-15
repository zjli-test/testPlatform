from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password

#登录
def loginView(request):
    title="登录";
    unit_2="/register";
    unit_2_name="立即注册";
    unit_1="/setpassword";
    unit_1_name="修改密码";
    if request.method == "POST":
        username= request.POST.get('username','');
        password=request.POST.get('password','');
        if User.objects.filter(username=username):
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                return redirect('/index')
            else:
                tips="账号密码错误，请重新输入"
        else:
            tips="用户不存在，请注册"
    return render(request, 'login.html', locals())

#注册
def registerView(request):
    title='立即注册'
    unit_2='/login'
    unit_2_name='立即登录'
    unit_1='/setpassword'
    unit_1_name='修改密码'
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if User.objects.filter(username=username):
            tips = '用户已存在'
        else:
            user = User.objects.create_user(username=username,password=password)
            tips = '注册成功，请登录'
    return render(request, 'register.html', locals())

#修改密码
def setpasswordView(request):
    title = '修改密码'
    unit_2 = '/login'
    unit_2_name = '立即登录'
    unit_1 = '/register'
    unit_1_name = '立即注册'
    if request.method == 'POST':
        username= request.POST.get('username','')
        old_password = request.POST.get('password','')
        new_password = request.POST.get('new_password','')
        if username and old_password and new_password:
            if old_password == new_password:
                tips = '新密码和旧密码不能相同'
            else:
                if User.objects.filter(username=username):
                    user = authenticate(username=username, password=old_password)
                    if user:
                        dj_ps = make_password(new_password, None, 'pbkdf2_sha256')
                        user.password = dj_ps
                        user.save()
                        tips = '密码修改成功'
                    else:
                        tips = '密码不正确'
                else:
                    tips = '用户不存在'
        else:
            tips = '用户名、密码和新密码不能为空'
    return render(request, 'setpassword.html', locals())

#退出登录
def logoutView(request):
    logout(request)
    return redirect('/login')

