from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "text", "created_date", "published_date")
    readonly_fields = ("created_date",)
