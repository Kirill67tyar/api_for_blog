from django.shortcuts import render
from .models import Post
# from .forms import PostForm
from django.views.generic import ListView
from django.http import JsonResponse, HttpResponse
from django.views.generic.detail import DetailView
from . import models




class PostListView(ListView):
    queryset = Post.objects.filter(status='published')
    context_object_name = 'posts'
    template_name = 'posts/post_list.html'



def article(request, pk):
    p = Post.objects.get(id=pk)
    return render(request, 'posts/article.html', {'article' : p})



# class PostArticleView(DetailView):
#     model = Post
#     template_name = 'article.html'



# errors for sentry-sdk:

def json_list_published_posts(request):
    posts = Post.objects.filter(status='published')

    # t = int('a') #-  error
    # 1 /0           #-  error
    context_posts = {
        'posts' :[
        {
            'title' : p.title,
            'slug' : p.slug,
            'id' : p.id,
            'published' : p.when_published,
        }
        for p in posts
                ]
                    }
    return JsonResponse(context_posts)



def trigger_error(request):
    pass
    # d = {'a':1}
    # return HttpResponse(d[-1])

# Create your views here.


