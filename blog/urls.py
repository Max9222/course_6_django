from django.urls import path
from main.urls import cache_page
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('blog/create/', cache_page(60)(BlogCreateView.as_view()), name='create_blog'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]