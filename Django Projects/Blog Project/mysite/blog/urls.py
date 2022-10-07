from django.urls import path
import blog.views as blog_views

# some usefull link                  --> 
# path converters                    : https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters
# re_path                            : https://docs.djangoproject.com/en/4.1/ref/urls/#django.urls.re_path
# regular expression in python       : https://docs.python.org/3/howto/regex.html
# url namespace in Django            : https://docs.djangoproject.com/en/4.1/topics/http/urls/#url-namespaces
# Django Template Language           : https://docs.djangoproject.com/en/4.1/ref/templates/language/
# built-in template tags and filters : https://docs.djangoproject.com/en/4.1/ref/templates/builtins/

# Note : Namespaces have to be unique across your entire project 
# this app_name is usefull for referring to these url from main url pattern 
app_name = 'BLOG'

urlpatterns = [
    path('',blog_views.all_published_post,name='post_list'),
    path('<int:id>/',blog_views.detail_published_post,name='post_detail')
]
