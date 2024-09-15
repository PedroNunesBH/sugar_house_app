from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nome")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensagem")
    