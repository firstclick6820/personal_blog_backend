from django.contrib import admin

# Register your models here.
from .models import Post, Category, Comment


class PostAdmin(admin.ModelAdmin):
    list_display =['title']
    prepopulated_fields = {'slug': ('title',)}




class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields= {'slug': ('title', )}
    
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    
    
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)