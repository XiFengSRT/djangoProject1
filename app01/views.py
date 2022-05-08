from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")
def use_html(request):
    return render(request,"use_html.html")
