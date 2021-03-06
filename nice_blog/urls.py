"""nice_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import (
    index, about, service, post, contact,single_post, search, create,post_update, post_delete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), 
    path('about/', about, name='about'),
    path('service/', service, name='service'),
    path('posts/', post, name='posts'),
    path('single-post/<id>/', single_post, name='post_details'),
    path('contact/', contact, name='contact'),
    path('tinymce/', include('tinymce.urls')),
    path('search/', search, name='search'),
    path('create/', create, name='create'),
    path('update/<id>/', post_update, name='update'),
    path('delete/<id>/', post_delete, name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)