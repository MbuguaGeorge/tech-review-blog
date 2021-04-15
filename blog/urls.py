from django.urls import path, reverse
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

name = 'blog'

urlpatterns = [
    path('trends/<slug:slug>/',views.trendpost, name = 'trendpost'),
    path('blog',views.blog, name = 'blog'),
    path('contact',views.contact, name = 'contact'),
    path('home',views.index, name = 'index'),
    path('blog/<slug:slug>/',views.blogpost, name = 'blog_post'),
    path('about',views.About, name='about'),
    path('', views.Confirm, name='confirm'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)