from django.shortcuts import render, HttpResponse
from django.views import View

# Create your views here.

# FBV
def login(request):
    if request.method == "GET":
        return HttpResponse("GET...")
    else:
        return HttpResponse("POST...")
    
# CBV
class LoginView(View):
    def get(self,request):
        return HttpResponse("LoginView GET...")
    
    def post(self,request):
        return HttpResponse("LoginView POST...")