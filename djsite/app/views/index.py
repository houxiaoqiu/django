from django.shortcuts import redirect, render


def index(request):
    #return HttpResponse("欢迎使用Django")
    return render(request,'index.html')

