from django.contrib import admin
from .models import *



# Register your models here.

class BlogCommentInline(admin.TabularInline):
    model = BlogComment
    extra = 1

@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ['post_id','title','category','pub_date']
    inlines = [BlogCommentInline]

    class Media:
        js = ('tinyInject.js',)






