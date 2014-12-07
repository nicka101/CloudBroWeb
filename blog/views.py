from django.shortcuts import render, loader
from django.http import HttpResponse
from blog.models import Post


def index(request):
    return render(request, 'blog/index.html')


def view_post(request, post_id):
    return HttpResponse("Blog post view")


def render_widget(post_count):
    return loader.render_to_string('blog/partial/blog_widget.html', {'posts': Post.objects.order_by('-created')[:post_count]})