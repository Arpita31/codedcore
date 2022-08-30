from urllib import request
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post, PostDetails, LanguagePostDetails

class PostListView(ListView):
    model = PostDetails
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = PostDetails
    template_name = 'blog/details.html'

    # def get_queryset(self):
    # #     # post_details = get_object_or_404(PostDetails, name=self.kwargs['name']).first()

    # #     # name = self.kwargs['name']
    # #     # queryset = super(PostDetailView, self).get_queryset()
    # #     # return queryset

    #     return PostDetails.objects.filter(name=self.kwargs['name'])

class LanguageListView(ListView):
    model = LanguagePostDetails
    template_name = 'blog/python.html'
    context_object_name = 'posts'

    def get_queryset(self): 
        return LanguagePostDetails.objects.filter(slug=self.kwargs['slug'])
    
