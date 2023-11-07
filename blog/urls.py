from django.urls import path
from .views import BlogCreateView, BlogUpdateView, BlogDeleteView, BlogDetailView, BlogListView

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('<slug:slug>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]