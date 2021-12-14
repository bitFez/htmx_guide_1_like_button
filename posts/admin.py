from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = Post
    fields = ['post_author', 'post_content', 'likes']

admin.site.register(Post, PostAdmin)