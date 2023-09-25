from django.contrib import admin
from articles.models import Article
from articles.models import Comment

admin.site.register(Article)
admin.site.register(Comment)
