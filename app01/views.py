from django.shortcuts import render, HttpResponse
import requests as req

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")


def use_html(request):
    # http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/05/news
        # 利用python获取数据，需要使用第三方库 requests
    results = req.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2022/05/news")
    date_list = results.json()
    print(date_list)
    return render(request, "use_html.html")
