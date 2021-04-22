from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)
PROGRAMMING = 'Programming'
CRYPTOCURRENCY = 'Cryptocurrency'
BLOCKCHAIN = 'Blockchain'
AI = 'Artificial Intelligence'
IOT = 'Internet of Things'
ML = 'Machine Learning'
CATEGORY = (
    (PROGRAMMING,'Programming'),
    (CRYPTOCURRENCY,'Cryptocurrency'),
    (BLOCKCHAIN,'Blockchain'),
    (AI,'Artificial Intelligence'),
    (IOT,'Internet of Things'),
    (ML,'Machine Learning')
)

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=255, unique=True, primary_key=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField('content')
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    thumbnail = models.ImageField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    category = models.CharField(choices=CATEGORY,max_length=50,default=PROGRAMMING,null=False)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Trend(models.Model):
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=255, unique=True,primary_key=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField('content')
    created_on = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    status = models.IntegerField(choices=STATUS,default=0)
    category = models.CharField(max_length=50,choices=CATEGORY,default=CRYPTOCURRENCY,null=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

class Message(models.Model):
    sender = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.sender

class Newsletter(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    confirmed = models.BooleanField(default=False)
    confirmation_number = models.CharField(max_length=15)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"