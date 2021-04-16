from django.forms import ModelForm
from django import forms
from .models import Message, Newsletter

class ContactForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

class SubscriberForm(forms.Form):
    email = forms.EmailField(label='Email:',
                            max_length=100,
                            widget=forms.EmailInput(attrs={'class': 'form-control'}))