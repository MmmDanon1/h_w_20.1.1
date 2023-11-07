from django.urls import path
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView, BlogListView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
]