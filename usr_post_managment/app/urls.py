from django.urls import path,include

from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView


urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<int:id>/', PostDetailView.as_view(),name="post_detail"),
    path('posts/<int:id>/edit', PostUpdateView.as_view(),name='post_edit'),
    path('posts/create/',PostCreateView.as_view()),
]
