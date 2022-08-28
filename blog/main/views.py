from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DetailView
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from main import models
import logging




logger = logging.getLogger(__name__)
# Create your views here




class BlogPostView(ListView):
    template_name = 'homepage.html'
    paginate_by = 12

    def get_queryset(self):
        blogposts = models.BlogPost.objects.active()
        return blogposts.order_by('-date_updated')

class BlogPostCategoryView(ListView):
    template_name = 'categoryview.html'
    paginate_by = 16
    model = models.BlogPost

    def get_queryset(self):
        slug = self.kwargs['slug']
        category = get_object_or_404(models.BlogPostCategory, slug=slug)

        blogpost = models.BlogPost.objects.filter(category = category)
        return blogpost


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        logger.info(slug)
        category = models.BlogPostCategory.objects.filter(slug = slug).first()

        context['other_books'] = [{'slug': x.slug, 'title': x.title, 'description': x.description} for x in models.BlogPost.objects.filter(category = category).all()]
        context['section'] = slug

        return context
    


class BlogDetailsView(DetailView):
    template_name = 'details.html'
    model = models.BlogPost

    def get_queryset(self):
        blogposts = models.BlogPost.objects.active()
        return blogposts.order_by('-date_updated')

    '''
    def get_context_data(self):
        context = super().get_context_data()
        logger.info(context)

        context['others'] = models.BlogPost.objects.active()

        return context
    '''