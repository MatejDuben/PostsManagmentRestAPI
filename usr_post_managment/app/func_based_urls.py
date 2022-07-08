from django.urls import include, path
from .func_based_views import list_posts,post_detail,post_create,post_update




urlpatterns = [
    path('posts/', list_posts),
    path('posts/<int:id>/', post_detail,name="post_detail"),
    path('posts/<int:id>/edit', post_update,name='post_edit'),
    path('posts/create/',post_create),
]
