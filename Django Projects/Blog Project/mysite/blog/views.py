from django.shortcuts import render
from blog.models import Post
from django.http import Http404


def all_published_post(request):
    posts = Post.published_posts.all()
    return render(request,
                  'blog/post/list.xhtml',
                  {'posts':posts})

def detail_published_post(request):
    try:
        post = Post.published_posts.filter(id=id)
    except post.DoesNotExist:
        raise 'Post with this id not found . please try again ...'
    return render(request,
                  'blog/post/detail.xhtml',
                  {'post':post})