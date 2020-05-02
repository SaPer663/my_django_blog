from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager


class PublishedManager(models.Manager): 
    def get_queryset(self): 
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = _('category')
        verbose_name_plural = _('categories')
    
    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (('draft', _('Draft')),('published', _('Published')))
    title = models.CharField(max_length=250, verbose_name=_('Title'))
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts', verbose_name=_('Author'))
    body = models.TextField(default='', verbose_name=_('body'))
    publish = models.DateTimeField(default=timezone.now, verbose_name=_('publish'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft',
                              verbose_name=_('status'))
    category = models.ForeignKey(Category,related_name='category',
                                 verbose_name=_('category'),
                                 on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name=_('image'))
    objects = models.Manager()
    published = PublishedManager()
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        #verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title  

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.publish.year,
                        self.publish.month, self.publish.day, self.slug])
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',
                              verbose_name=_('post'))
    name = models.CharField(max_length=80, verbose_name=_('name'))
    email = models.EmailField(verbose_name=_('email'))
    body = models.TextField(verbose_name=_('body'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('updated'))
    active = models.BooleanField(default=True, verbose_name=_('active'))

    class Meta:
        ordering = ('created',)
       # verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'



        
