from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Blog,Trend,Newsletter,Message
from .forms import ContactForm, SubscriberForm
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Create your views here.

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

def About(request):
    return render(request, 'blog/About.html')

def contact(request):
    if request.method == 'POST':
        form_a = ContactForm(request.POST)
        if form_a.is_valid():
            form_a.save()
            return HttpResponseRedirect('home')
    else:
        form_a = ContactForm()
        return render(request, 'blog/contact.html', {'form_a' : form_a})

def random_digits():
    return "%0.6d" % random.randint(0, 999999)

@csrf_exempt
def blog(request):
    b = Blog.objects.filter(status=1).order_by('-created_on')
    if request.method == 'POST':
        sub = Newsletter(email=request.POST['email'], confirmation_number=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for subscribing to my email newsletter! \
                Please complete the process by \
                <a href="{}/?email={}&confirmation_number={}"> clicking here to \
                confirm your registration </a>.'.format(request.build_absolute_uri('confirm'),
                sub.email,
                sub.confirmation_number))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'blog/confirm.html', {'email':sub.email, 'action' : 'A confirmation message has been sent to your email. Click the link to confirm your registration','form' : SubscriberForm()})
    else:
        return render(request, 'blog/Blog.html', {'b' : b,'form': SubscriberForm()})

def Confirm(request):
    sub = Newsletter.objects.get(email=request.GET['email'])
    if sub.confirmation_number == request.GET['confirmation_number']:
        sub.confirmed = True
        sub.save()
        return render(request, 'blog/confirm.html', {'email':sub.email, 'action':'Thank you for subscribing to my email newsletter'})
    else:
        return render(request, 'blog/confirm.html', {'email':sub.email, 'action':'Sorry, your email was denied. Try entering a valid email address.'})