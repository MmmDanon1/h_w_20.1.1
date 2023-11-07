from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Blog
from django.urls import reverse_lazy


class BlogCreateView(CreateView):
    model = Blog
    fields = ['name', 'slug', 'description', 'preview', 'is_publish']
    success_url = reverse_lazy('blog_list')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['name', 'slug', 'description', 'preview', 'is_publish']
    success_url = reverse_lazy('blog_list')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')


class BlogDetailView(DetailView):
    model = Blog

class BlogListView(ListView):
    model = Blog