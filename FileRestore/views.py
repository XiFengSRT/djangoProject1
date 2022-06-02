from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def toRequestHtml(request):
    return render(request, request.GET.get('productName') + '.html')
