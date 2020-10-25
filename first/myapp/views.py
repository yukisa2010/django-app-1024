# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Hello World', charset='cp932')
    context = {
        'name':'Yuki Sato'
    }
    return render(request,'myapp/index.html', context)