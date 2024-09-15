from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm

class HomeView(TemplateView):
    template_name = "base.html"


class AboutUsView(TemplateView):
    template_name = "about_us.html"


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm


class MenuView(TemplateView):
    template_name = "menu.html"
