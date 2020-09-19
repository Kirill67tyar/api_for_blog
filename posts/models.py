from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Можно будет сделать, чтобы пользователь сам вводил ту категорию,
# которая ему нужна через форму, на отдельной странице,
# а не выбирал из CATEGORIES_CHOICES
class Categories(models.Model):

    CATEGORIES_CHOICES = (
                ('news', 'Новости'),
                ('economics', 'Экономика'),
                ('science', 'Наука'),
                ('tech', 'Техника'),
                ('it', 'IT'),
                ('none', 'Без категории'),
                ('sport', 'Спорт'),
            )

    title = models.CharField(max_length=30, choices=CATEGORIES_CHOICES, default='none')
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return f'Категория: {self.title}'

    # class Meta:
    #
    #     verbose_name = 'Категория'
    #     verbose_name_plural = 'Категории'



class Post(models.Model):

    STATUS_CHOICES = (
                        ('draft', 'Черновик'),
                        ('published', 'Опубликован')
                      )
    title          = models.CharField(max_length=250)
    slug           = models.SlugField(max_length=250, unique_for_date='when_published') # вот это поле должно быть уникальным бля
    author         = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body           = models.TextField()
    when_published = models.DateTimeField(default=timezone.now)
    created        = models.DateTimeField(auto_now_add=True)
    updated        = models.DateTimeField(auto_now = True)
    status         = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # как мне видится - связка ManyToMany здесь предпочтительнее
    # в будущем - поменять
    category       = models.ForeignKey(Categories,
                                       related_name='posts',
                                       null=True, blank=True,
                                       on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

# Create your models here.
