from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'slug', 'description', 'preview', 'is_publish']
    success_url = '/blog/'


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name', 'slug', 'description', 'preview', 'is_publish']
    success_url = '/blog/'


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'


class BlogDetailView(DetailView):
    model = Blog

class BlogListView(ListView):
    model = Blog