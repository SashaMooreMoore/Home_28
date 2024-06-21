from django.contrib import admin
from .models import Article

@admin.register(Article)
class InfoAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'is_draft', 'is_deleted', 'published_date']
    list_display_links = ['title', 'content', 'is_draft', 'is_deleted', 'published_date']
