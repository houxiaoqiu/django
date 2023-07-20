""" drddemo 子路由 """

from rest_framework.routers import DefaultRouter

from . import views

urlpatterns = []

router = DefaultRouter()    # 可处理视图的路由
router.register('students',views.StudentViewSet)    # 向路由注册视图集
router.register('books',views.BookViewSet)
router.register('publishes',views.PublishViewSet)
router.register('naturalperson',views.NaturalPersonView)
router.register('legalperson',views.LegalPersonView)
router.register('employee',views.EmployeeView)
router.register('user',views.UserView)
router.register('department',views.DepartmentView)

urlpatterns += router.urls  # 将此子路由信息追加到主路由列表中

