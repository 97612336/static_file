import json
import os

import logging
from django.shortcuts import render

# Create your views here.
from static_file.settings import STATIC_ROOT, STATIC_PATH_URL


# 去往文件主页
def index(request):
    # 得到该目录下的所有文件和文件夹
    file_list = os.listdir(STATIC_ROOT)
    # 得到url的路径
    static_url = STATIC_PATH_URL
    res = {
        "file_list": file_list,
        'static_url': static_url
    }

    return render(request, "index.html", res)


# 上传文件到静态空间
def upload_file(request):
    # 得到上传的参数
    username = request.POST.get("username")
    password = request.POST.get("password")
    # 得到家目录路径
    home_path = os.getenv("HOME")
    upload_allow_info_path = home_path + "/.static_file_info"
    # 读取配置文件信息
    with open(upload_allow_info_path, 'r') as f1:
        upload_allow_info = f1.read()
    user = json.loads(upload_allow_info)
    # 执行验证
    right_username = user.get('username')
    right_password = user.get('password')
    # 执行判断,如果两个值相等,则执行保存文件的操作
    if right_username == username and right_password == password:
        # 接收前端传来的文件
        file = request.FILES.get("file")
        save_upload(file)
        return render(request, "index.html")
    else:
        return render(request, 'err.html')


# 将上传文件存储到本地的操作
def save_upload(file):
    file_name = file.name
    root_path = STATIC_ROOT
    file_save_path = root_path + '/' + file_name
    with open(file_save_path, 'wb+') as f2:
        for one in file.chunks():
            f2.write(one)

