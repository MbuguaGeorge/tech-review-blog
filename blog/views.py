from django.shortcuts import render
from .models import Blog,Trend

# Create your views here.

def blog(request):  
    b = Blog.objects.filter(status=1).order_by('-created_on')
    context = {
        'b' : b,
    }
    return render(request, 'blog/Blog.html', context)

def contact(request):
    return render(request, 'blog/contact.html')

def index(request):
    t = Trend.objects.filter(status=1).order_by('-created_on')
    context = {
        't' : t,
    }
    return render(request, 'blog/index.html', context)

def blogpost(request, slug):
    post = Blog.objects.filter(pk=slug).first()
    context = {
        'post' : post,
    }
    return render(request, 'blog/blogpost.html',context)

def trendpost(request, slug):
    trendy = Trend.objects.filter(pk=slug).first()
    context = {
        'trendy' : trendy,
    }
    return render(request, 'blog/trendpost.html',context)