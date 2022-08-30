from pipes import Template
from django.urls import path
from django.views.generic import TemplateView

from .views import PostListView, PostDetailView, LanguageListView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('<slug:slug>/', LanguageListView.as_view(), name='blog-python'),
    path('about/', TemplateView.as_view(template_name="blog/about.html"), name='blog-about'),
    path('<slug:slug>/', PostDetailView.as_view(), name='blog-details'),
]