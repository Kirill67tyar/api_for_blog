"""blog URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from posts.views import PostListView, json_list_published_posts
from posts.api import views as api_view
from django.conf import settings
from posts import views
from posts import api


urlpatterns = [
    path('sentry-debug/', views.trigger_error),
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('api-old/posts/', json_list_published_posts),
    path('api/', include('posts.api.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]


# !!! Не сделал сохранение во вьюшке в API поля ForeignKey
# Не сохраняет категории, собственно при добавлении категорий






















