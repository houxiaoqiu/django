""" drddemo 子路由 """
from django.urls import path,re_path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView,\
    TokenVerifyView,TokenObtainPairView
from django.views.decorators.cache import cache_page
from . import views
from common import FileView

urlpatterns = [
    path('api/login/',views.AdminLoginView.as_view()),       # api/登录
    path('api/logout/',views.LogoutView.as_view()),       # api/退出
    path('login/',views.LoginView.as_view()),       # 登录
    path('register/',views.RegisterView.as_view()),     # 注册
    path('token/verify/', TokenVerifyView.as_view()),      # 校验 Token
    path('token/refresh/', TokenRefreshView.as_view()),     # 刷新 Token
    path('users/<int:pk>/', cache_page(60)(views.UserView.as_view({'get':'retrieve'}))),    # 获取指定用户信息
    path('users/<int:pk>/avatar/upload', views.UserView.as_view({'post':'upload_avatar'})),    # 上传用户头像
    re_path(r'media/(.+?)/',FileView.ImageView.as_view()),  
    path('address/',views.AddrVeiw.as_view({
        "post":"create","get": "list"
        })),     # 地址
]

router = DefaultRouter()    # 可处理视图的路由
router.register('students',views.StudentViewSet)    # 向路由注册视图集
router.register('books',views.BookViewSet)
router.register('publishes',views.PublishViewSet)
router.register('naturalperson',views.NaturalPersonView)
router.register('legalperson',views.LegalPersonView)
router.register('employee',views.EmployeeView)
router.register('user',views.UserView)
router.register('department',views.DepartmentView)
# router.register('media/(.+?)',FileView.FielView)

urlpatterns += router.urls  # 将此子路由信息追加到主路由列表中

