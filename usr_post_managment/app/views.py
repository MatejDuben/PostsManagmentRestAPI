from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from .serializer import PostSerializer,PostUpdateSerializer
from .models import Post

import requests


class PostListView(ListAPIView):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer
  

class PostDetailView(RetrieveAPIView):
    serializer_class = PostSerializer
    lookup_field = "id"

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset

    def get(self,request, id, *args, **kwargs):
        if self.get_queryset().filter(id=id).exists():
            post = self.get_object()
        else:
            #vyhladavanie v externej API
            api_url = "https://jsonplaceholder.typicode.com/posts"
            response = requests.get(api_url)
            data = response.json()
            for i in data:
                if id == int(i['id']):
                    Post.objects.create(id=id,user_id=i['userId'],title=i['title'],body=i['body']).save()
            post = self.get_object()

        serializer = self.get_serializer(post)
        return Response(serializer.data)


class PostUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = "id"

class PostCreateView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer