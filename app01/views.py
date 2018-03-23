from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    """进入首页"""

    # 演示500错误
    # print('aa' + None)

    # 获取request对象中的一些属性
    path = request.path
    method = request.method
    encoding = request.encoding

    text = 'path=%s, method=%s, encoding=%s' % (path, method, encoding)
    return HttpResponse(text)

def post(request):

    return render(request,"post.html")

def get_post(request):
    username = request.POST.get("username")

    password = request.POST.get("password")

    gender = request.POST.get("gender")

    hobby = request.POST.getlist("hobby")

    text = "username = %s,<br/>"% + "password = %s,<br/>" +"gender = %s,<br/>" +"hobby = %s,<br/>" % hobby
    # text = 'username=%s, <br/> '\
    #        'password=%s, <br/>' \
    #        'gender=%s, <br/>' \
    #        'hobby=%s, <br/>' \
    #        % (username, password, gender, hobby)
    return HttpResponse(text)



# Create your views here.
