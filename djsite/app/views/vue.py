from django.shortcuts import redirect, render,HttpResponse


def vue_test01(request):
    return render(request,"vue_test01.html")