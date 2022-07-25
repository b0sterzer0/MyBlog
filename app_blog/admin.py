from django.contrib import admin
from .models import PostModel


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'add_date']


admin.site.register(PostModel, PostAdmin)
