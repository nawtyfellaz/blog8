"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  path('blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.urls import path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from accounts.views import (login_view, register_view, logout_view)


urlpatterns = [
    path('contact/', include("contact.urls")),
    path('admin/', admin.site.urls),
    path('comments/', include("comments.urls")),
    
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include("posts.urls")),
    #path('posts/$', "<appname>.views.<function_name>"),
    path('robots\.txt', TemplateView.as_view(template_name='src/robots.txt', content_type='text/plain')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)