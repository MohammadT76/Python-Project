from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# for slug field
from django.utils.text import slugify

class Post(models.Model):
    # usefull link for Model field : 
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300)
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    
    # for more info about this function see this link : 
    # https://stackoverflow.com/questions/38963193/auto-populate-slug-field-django
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)
    
    # adding status field
    # for more information aboute defining status field , please see these links : 
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
    # https://docs.python.org/3/library/enum.html
    # some tips about Status class that define in the following lines : 
    # 1) Post.Status.choices --> to obtain the available choices
    # 2) Post.Status.labels  --> to obtain the human-readable names
    # 3) Post.Status.values  --> to obtain the actual values of the choices
    class Status(models.TextChoices):
        DRAFT = 'D','Draft'
        PUBLISH = 'P','Publish'
    status = models.CharField(max_length=1,choices=Status.choices,default=Status.DRAFT)
    
    class Meta:
        ordering = [
            '-published'
        ]
        # indexes : This will improve performance for queries filtering 
        # or ordering results by this (or these) field(or fields)
        indexes = [
            models.Index(fields=['-published'])
        ]
    
    def __str__(self):
        return self.title
    