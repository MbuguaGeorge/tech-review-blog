from django.contrib import admin
from .models import Blog, Trend

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}

class TrendAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','status', 'updated_on')
    prepopulated_fields = {'slug':('title',)}

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Trend,TrendAdmin)