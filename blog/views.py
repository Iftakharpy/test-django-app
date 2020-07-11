from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def all_blogs(request):
    # blogs = models.Blog.objects.all() #sorted by primary key
    blogs = models.Blog.objects.order_by('-pk')[:10] #sorted by date descending and gets latest 10 blogs
    return render(request, 'all_blogs.html', {'blogs':blogs})

def blog_num(request, blog_pk):
    blog = get_object_or_404(models.Blog, pk=blog_pk)
    return render(request, 'blog.html', {'blog':blog})