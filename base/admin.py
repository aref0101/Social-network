from django.contrib import admin
from .models import customUser, Post, Comment

# Register your models here.

admin.site.register(customUser)
admin.site.register(Post)
admin.site.register(Comment)