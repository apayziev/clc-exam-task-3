from django.contrib import admin
from article.models import Article, Comment, Tag, Bookmark

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Bookmark)
