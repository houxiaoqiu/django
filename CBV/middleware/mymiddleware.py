import re
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print('MyMW process_request do ---')
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('MyMW process_view do ---')
    def process_response(self, request, restponse):
        print('MyMW process_response do ---')

class VisitLimit(MiddlewareMixin):
    visit_times = {}
    def process_request(self, request):
        ip_address = request.META['REMOTE_ADDR']
        path_url = request.path_info
        if not re.match('^/admin', path_url):
            return
        times =  self.visit_times.get(ip_address, 0)
        print('ip', ip_address, '已经访问',times)
        self.visit_times[ip_address] = times + 1
        if times < 5 :
            return 
        return HttpResponse('因已连续访问该地址' + str(times) + '次, 被禁止访问。')
