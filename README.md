# django
learning from django.


Backends
    创建python虚拟环境
        python -m venv <.venv>
    安装后端开发环境
        pip install django
        pip install djangorestframework
        pip install django-cors-headers
    创建django项目
        django-admin startproject <backends> 
    切换django项目目录
        cd backends
    创建django应用
        python manage.py startapp lyb
    启动后端服务
        python manage.py runserver

Frontends
    node （windows安装：.msi）
    npm instll axios
    创建vue3项目
        npm init vite-app <frontends>
    切换vue3项目目录: 
        cd frontends
    安装相应依赖
        npm install
    启动服务
        npm run dev 


RBAC权限管理
    数据结构
        一级菜单（目录）：id, title, icon
        二级菜单（路由）：id, title, _id(目录id), router, is_menu
        用户：id, user
        角色：id, role
        用户角色：id, user_id, role_id
        权限：id, url_name, method, permission, router_id 
        角色权限：id, role_id, permission_id
    功能
        根据用户信息获取权限
            permmision = {
                "depart-list": ["GET", "POST"],
                "depart-detail": ["GET", "POST", "PUT", "DELETE"],
            }
        根据用户信息获取路由列表
            router = [
                "basic1",
                "basic2",
                "basic3",
            ]
        根据用户信息获取菜单信息
            menu = [
                {
                    id: 1,
                    titile: "权限管理",
                    icon: "setting",
                    children: [
                        {id: 1, name: "xxx", title: "菜单管理"},
                        {id: 2, name: "xxx", title: "用户管理"},
                    ],
                },
                {
                    id: 2,
                    titile: "VIP中心",
                    icon: "setting",
                    children: [
                        {id: 3, name: "xxx", title: "订单管理"},
                        {id: 4, name: "xxx", title: "销售管理"},
                    ],
                },
            ]
    动态菜单 menu
    页面访问权限 router
    功能按钮权限 
            