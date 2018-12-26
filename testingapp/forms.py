
from django import forms



class ContactForm(forms.Form):

    subject  = forms.CharField(max_length=20 , required=True)
    email    = forms.EmailField(max_length= 30 , required= False)
    message  = forms.CharField(widget=forms.Textarea, required=True)









