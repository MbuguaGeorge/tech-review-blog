from django.shortcuts import render
from .models import Blog,Trend

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def blog(request):  
    b = Blog.objects.filter(status=1).order_by('-created_on')
    context = {
        'b' : b,
    }
    return render(request, 'blog/Blog.html', context)

def contact(request):
    return render(request, 'blog/contact.html')

def trends(request):
    t = Trend.objects.all()
    context = {
        't' : t,
    }
    return render(request, 'blog/Trends.html', context)