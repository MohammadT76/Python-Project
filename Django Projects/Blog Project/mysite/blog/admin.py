from django.contrib import admin
from blog.models import Post

# usefull link : https://docs.djangoproject.com/en/4.1/ref/contrib/admin/

# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','published','created','updated','author','status']
    list_editable = ['title','status']
    list_filter = ['created','updated','status','published']
    search_fields = ['title','body']
    raw_id_fields = ['author']
    prepopulated_fields = {'slug':('title','status')}
    date_hierarchy = 'published'
    ordering = ['status','published']
