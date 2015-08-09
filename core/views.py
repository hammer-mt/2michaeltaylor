from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class LandingView(TemplateView):
	template_name = 'base/index.html'

class AboutView(TemplateView):
	template_name = 'base/about.html'

class ContactView(TemplateView):
	template_name = 'base/contact.html'

class PostView(TemplateView):
	template_name = 'base/post.html'