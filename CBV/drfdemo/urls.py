""" drddemo 子路由 """

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = []

router = DefaultRouter()    # 可处理视图的路由
router.register('students',views.StudentViewSet)    # 向路由注册视图集
router.register('books',views.BookViewSet)
router.register('publishes',views.PublishViewSet)

urlpatterns += router.urls  # 将此子路由信息追加到主路由列表中

