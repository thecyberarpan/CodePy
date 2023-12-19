from django import forms

class SubscriberForm(forms.Form):
    CallToAction = forms.EmailField()
