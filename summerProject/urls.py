"""homework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from garden import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('cv/', views.cv, name="cv"),
    path('cv/login', views.cvLog, name='login'),
    path('cv/edit', views.cvEdit, name='cvEdit'),
    path('cv/edit/project', views.proAdd, name='proAdd'),
    path('cv/edit/education', views.eduAdd, name='eduAdd'),
    path('cv/edit/interest', views.intAdd, name='intAdd'),
    path('blog/', views.blog, name='blog'),
    path('blog/tag', views.tagBlog, name="tagBlog"),
    path('blog/article', views.Article, name="article"),
    path('blog/edit', views.editer, name='editor')
]
