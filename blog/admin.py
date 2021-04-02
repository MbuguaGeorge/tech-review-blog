from django.contrib import admin
from .models import Blog, Trend

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}

class TrendAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated_on')

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Trend,TrendAdmin)