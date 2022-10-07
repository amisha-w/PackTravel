"""PackTravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
import imp
from user import views as userView
from django.contrib import admin
from django.urls import path
from search import views as searchViews
from publish import views as publishViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', searchViews.search_index, name = 'search'),
    path('publish/', publishViews.publish, name = 'publish'),
    path('index/', userView.index, name ='index'),
    path('index/<username>',userView.index, name='index'),
    path('register/', userView.register, name='register'),
    path('logout/', userView.logout, name='logout'),
    path('login/', userView.login, name='login'),
    path('route/', publishViews.route, name='route')
]
