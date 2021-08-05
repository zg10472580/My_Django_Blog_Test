"""BlogTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog.views import *
from blog.tool import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('PaiHang', PaiHang),
    path('blog/detail/<int:pk>/', Get_Tiezi),
    path('blog/archive/', archive),
    path('blog/search/', Search_Index),
    path('blog/Ret_Tag/<str:name>/', Ret_Tag),
    path('blog/Ret_author/<str:name>/', Ret_author),
    path('blog/category/<str:name>/', category),
    path('tool/', tool_index),
    path('Get_Fenlei/', Get_Fenlei),
    path('login/', LogIn),
    path('Register/', Register),
    # path('blog_commenced/<int:pk>/', blog_commenced),
    # path('detail/<int:pk>/', detail, name='detail'),

]
