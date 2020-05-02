from django import template
from django.db.models import Count
from ..models import Post


register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments'))\
                                  .order_by('-total_comments')[:count]


@register.simple_tag
def get_the_number_of_comments_per_post(post):
    return post.comments.count()

@register.simple_tag
def get_day_and_month_of_post_publication(post):
    return post.publish.strftime("%d %B ")