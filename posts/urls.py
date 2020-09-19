
from . import views
from django.urls import path


app_name = 'posts'

urlpatterns = [
    path('list/', views.PostListView.as_view(), name='list'),
    path('article/<int:pk>', views.article, name='article'),
]
