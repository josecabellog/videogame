from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CategoryPageView(TemplateView):
    template_name = 'categories.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'