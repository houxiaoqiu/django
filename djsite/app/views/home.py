<<<<<<< HEAD
from django.shortcuts import redirect, render


def index(request):
    #return HttpResponse("欢迎使用Django")
    return render(request,'index.html')

=======
from django.shortcuts import redirect, render,HttpResponse

def index(request):
    return render(request,'index.html')
>>>>>>> 562b281bc1794c7a30b47012c8c7fb141b1b5fc1
