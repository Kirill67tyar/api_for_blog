from rest_framework import serializers
from posts.models import Post, Categories
from django.contrib.auth.models import User





class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'username', 'email'





class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categories
        fields = 'title', 'slug',




class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(many=False, read_only=True)

    category = CategoriesSerializer(many=False, read_only=True) # add argument read_only=True

    class Meta:
        model = Post
        fields = 'id', 'title', 'slug', 'author', 'category',



