from posts.models import Post, Categories
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from.serializers import PostSerializer, CategoriesSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin





class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer






class CategoriesListView(generics.ListAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer





# class CategoryView(generics.ListAPIView):
#     serializer_class = PostSerializer
#
#     def get_queryset(self): #, category):   # мой вариант - попробовать передать category в аргументы
#         #                     увы, но мой вариант не работает
#
#         category = self.kwargs['category'] # - не мой вариант
#         # скорее всего этот kwargs берется из значение, которое мы передаем в url
#         #в данном случае category в <> - api/categories/<slug:category>
#
#         # консоль
#         print(f'\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n'
#               f'self.kwargs - {self.kwargs}'
#               f'\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n')
#
#         queryset = Post.objects.filter(category__title=category)
#
#         return queryset


class CategoryView(LoginRequiredMixin, APIView):
    def get(self, request, category=None):

        if category:
            all_posts = Post.objects.filter(author=request.user).filter(category__slug=category)
            serializer = PostSerializer(all_posts, many=True)


            # post = get_object_or_404(Post, author=request.user, category__slug=category)
            # serializer = PostSerializer(post) # если all_posts вместо post, то добавь many=True
        #     как дополнительный параметр. Статья то может быть не одна, поэтому all_posts
        #       здесь больше имеет смысла

        else:
            all_posts = Post.objects.filter(author=request.user).all()
            serializer = PostSerializer(all_posts, many=True)

        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        # консоль
        print(f'\n\nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n'
              f'request.data - {request.data}'
              f'\nzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz\n\n')

        if serializer.is_valid():
            # new_post = serializer.save(commit=False)  - такое сохранения при сиреалайзерах неправильное
            # new_post.author = request.user
            # new_post.save()
            # консоль:

            serializer.save(author=request.user) # - такое правильное
            # категории не сохраняет, потому что для сохранения ForeignKey - требуется отдельный метод
            # типа как для many to many - save_m2m()
            # как сохраняются ForeignKey? смотри в документации, наводка:
            # >> > from blog.models import Blog, Entry
            # >> > entry = Entry.objects.get(pk=1)
            # >> > cheese_blog = Blog.objects.get(name="Cheddar Talk")
            # >> > entry.blog = cheese_blog
            # >> > entry.save()
            title = request.data['category']['title']
            slug = request.data['category']['slug']
            cat = Categories.objects.filter(title=title).filter(slug=slug)
            object = Post.objects.get(title=request.data['title'])

            if cat:
                object.category = cat[0]

            else:
                new_category = Categories.objects.create(title=title, slug=slug)
                object.category = new_category
            object.save()
# В общем и целом добавление новых слагов через api работает, так-же как и создание новых постов
# и привязка их к уже существующим слагам
# но нужно быть аккуратным: slug из Post должен быть каждый раз уникальным
# потому что slug из Post привязан к экземплярам класса Post
# slug из Category не должен дублироваться, т.к. там не стоит unique=True (хотя надо проверить)
#
# а slug из Categories не должен содержать слешей (мб деффисы может содержать)
# Вообще слаги вещь нужная, но для новичка слишком сложная, т.к. имеет свою специфику


            print(f'\n\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n'
                  f'serializer.data - {serializer.data}'
                  f'\nvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv\n\n')

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, category):
        post = get_object_or_404(Post, author=request, category__slug=category)
        serializer = PostSerializer(post)
        data = serializer.data
        serializer.delete()
        return Response(data)


        pass







