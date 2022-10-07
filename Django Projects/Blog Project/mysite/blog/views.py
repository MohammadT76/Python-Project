from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.http import Http404


def all_published_post(request):
    posts = Post.published_posts.all()
    return render(request,
                  'blog/post/post_list.xhtml',
                  {'posts':posts})

def detail_published_post(request):
    # try:
    #     post = Post.published_posts.filter(id=id)
    # except post.DoesNotExist:
    #     raise 'Post with this id not found . please try again ...'
    # you can use the above code or the following code : 
    post = get_object_or_404(Post,
                             id=id,
                             status=Post.Status.PUBLISH)
    return render(request,
                  'blog/post/post_detail.xhtml',
                  {'post':post})