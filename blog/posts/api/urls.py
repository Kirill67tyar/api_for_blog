from django.urls import path
from . import views as api_view


urlpatterns = [
    path('posts/', api_view.PostListView.as_view(), name='api_post_list'), #http://127.0.0.1:8000/api/posts/
    path('posts/<pk>', api_view.PostDetailView.as_view(), name='api_post_detail'),
    path('categories/', api_view.CategoryView.as_view(),    # http://127.0.0.1:8000/api/categories/
         name='api_categories_list'),
    path('categories/<slug:category>', api_view.CategoryView.as_view(),
             name='api_category'),
    # path('categories/', api_view.CategoriesListView.as_view(),
    #      name='api_categories_list'),
]