from django import forms

class GreetingForm(forms.Form):
    message_text = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Enter a greeting'}), max_length=255)