from django.db import models
from common.models import User
from helpers.models import BaseModel


# Create your models here.

class Tag(BaseModel):
    slug = models.CharField(max_length=128, unique=True)
    tag_name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=128, verbose_name='Sub_title')
    content = models.TextField()
    
    published_datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    image = models.ImageField(upload_to="articles/", null=True, blank=True)
    image_caption = models.CharField(max_length=128, null=True, blank=True)
    
    read_time = models.IntegerField(default=0)
    views_count = models.PositiveIntegerField(default=0)

    is_popular = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    is_for_you = models.BooleanField(default=False)

    tags = models.ManyToManyField(Tag, blank=True, related_name='articles')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'articles'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.content
    
    class Meta:
        db_table = 'comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Bookmark(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.article.title
    
    class Meta:
        db_table = 'bookmarks'
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'