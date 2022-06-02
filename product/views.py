from django.shortcuts import render

import User.models
from product.models import product, property
from User.models import User as user
from recharge.models import rechargeRequest
from django.http import HttpResponse
from django.http import FileResponse
import os
import time


# Create your views here.
def showPage(request):
    loginMessage = "Failure"
    data_list = product.objects.all()
    # print(data_list)
    final = []
    for data in data_list:
        final.append(
            [data.showName, data.description, data.price, data.html_address, data.css_address, data.js_address,
             data.png_address])
    return render(request, "showPage.html", {"final": final, "loginMessage": loginMessage})


def register(request):
    username = request.GET.get("username")
    pwd = request.GET.get("pwd")
    showName = request.GET.get("showName")
    user.objects.create(userName=username, password=pwd, showName=showName, wallet=0)
    return render(request, "showPage.html")


def login(request):
    data_list = product.objects.all()  # 获取所有产品的记录
    # -------------获取用户登录的用户名和密码-------------
    username = request.GET.get("username")
    pwd = request.GET.get("pwd")
    # -------------获取用户登录的用户名和密码-------------
    tempUser = user.objects.filter(userName=username).first()  # 验证用户名和密码是否匹配
    wallet = tempUser.wallet  # 获取用用户的余额
    isBreak = 0
    if tempUser.password == pwd:
        loginMessage = "Succeed"
        property_list = property.objects.filter(userName=username).all()

        property_userName = {}
        for data in data_list:
            is_show = False
            for property_iterator in property_list:
                if is_show == False and data.showName == property_iterator.productName:
                    property_userName[data.showName] = False
                    is_show = True
            if is_show == False:
                property_userName[data.showName] = True
        final = []
        for data in data_list:
            if property_userName[data.showName] == True:
                final.append(
                    [data.showName, data.description, data.price, data.html_address, data.css_address, data.js_address,
                     data.png_address, True])
            else:
                final.append(
                    [data.showName, data.description, data.price, data.html_address, data.css_address, data.js_address,
                     data.png_address, False])
        print(property_userName)
        return render(request, "showPage.html",
                      {"loginMessage": loginMessage, "username": username, "wallet": wallet, "final": final})
    else:
        loginMessage = "Failure"
        return render(request, "showPage.html", {"loginMessage": loginMessage})


def recharge(request):
    rechargeUser = request.GET.get("rechargeUser")
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    recharge = request.GET.get("recharge")
    rechargeRequest.objects.create(userName=rechargeUser, date=date, recharge=recharge, accpet=0)
    loginMessage = "Succeed"
    data_list = product.objects.all()  # 获取所有产品的记录
    # -------------获取用户登录的用户名和密码-------------
    username = request.GET.get("rechargeUser")
    tempUser = user.objects.filter(userName=username).first()  # 验证用户名和密码是否匹配
    wallet = tempUser.wallet  # 获取用用户的余额

    property_list = property.objects.filter(userName=username).all()

    property_userName = {}
    for data in data_list:
        is_show = False
        for property_iterator in property_list:
            if is_show == False and data.showName == property_iterator.productName:
                property_userName[data.showName] = False
                is_show = True
        if is_show == False:
            property_userName[data.showName] = True
    final = []
    for data in data_list:
        if property_userName[data.showName] == True:
            final.append(
                [data.showName, data.description, data.price, data.html_address, data.css_address, data.js_address,
                 data.png_address, True])
        else:
            final.append(
                [data.showName, data.description, data.price, data.html_address, data.css_address, data.js_address,
                 data.png_address, False])
    print(property_userName)
    return render(request, "showPage.html",
                  {"loginMessage": loginMessage, "username": username, "wallet": wallet, "final": final})


def purchase(request):
    tempUser = user.objects.filter(userName=request.GET.get("username")).first()
    # tempUser.
    tempProduct = product.objects.filter(showName=request.GET.get("productName")).first()
    date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    loginMessage = "Succeed"
    return render(request, "purchasePage.html",
                  {"loginMessage": loginMessage, "tempUser": tempUser, "tempProduct": tempProduct, "time": date})


def deal(request):
    productName = request.GET.get("productName")
    userName = request.GET.get("userName")
    tempUser = user.objects.filter(userName=userName).first()
    if tempUser.wallet > int(request.GET.get("price")):
        property.objects.create(userName=userName, productName=productName)
        tempUser.wallet = tempUser.wallet - int(request.GET.get("price"))
        tempUser.save()
        data_list = product.objects.all()
        property_list = property.objects.filter(userName=userName).all()
        dealMassage = "yes"
        return render(request, "purchasePage.html",
                      {"username": tempUser.userName, "wallet": tempUser.wallet, "data_list": data_list,
                       "property_list": property_list, "dealMassage": dealMassage})
    else:
        dealMassage = "余额不足"
        tempProduct = product.objects.filter(showName=request.GET.get("productName")).first()
        loginMessage = "Succeed"
        date = request.GET.get("date")
        return render(request, "purchasePage.html",
                      {"loginMessage": loginMessage, "tempUser": tempUser, "tempProduct": tempProduct, "time": date,
                       "dealMassage": dealMassage})


def download(request):
    dir, filename = os.path.split(request.GET.get("file"))
    file = open(request.GET.get("file"), 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{}"'.format(filename)
    return response


def downPage(request):
    downloadFiles = {}
    if "none" != request.GET.get("jsFile"):
        downloadFiles["js"] = request.GET.get("jsFile")
    if "none" != request.GET.get("cssFile"):
        downloadFiles["css"] = request.GET.get("cssFile")
    if "none" != request.GET.get("htmlFile"):
        downloadFiles["html"] = request.GET.get("htmlFile")
    return render(request, "downPage.html", {"downloadFiles": downloadFiles})
