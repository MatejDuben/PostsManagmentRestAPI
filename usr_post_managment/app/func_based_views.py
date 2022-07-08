from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from .models import Post
from .serializer import PostSerializer,PostUpdateSerializer
import json, requests

from rest_framework.request import Request
from rest_framework.test import APIRequestFactory




@api_view(["GET"])
def list_posts(request):
    
    serializer_context = {
        'request': request,
    }

    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True, context=serializer_context)
    return Response(serializer.data)



@api_view(["GET"])
def post_detail(request, id):
    serializer_context = {
        'request': request,
    }

    if Post.objects.filter(id=id).exists():
        post = Post.objects.filter(id=id)
    else:
        #vyhladavanie v exterenj API 
        api_url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(api_url)
        data = response.json()
        for i in data:
            if id == int(i['id']):
                Post.objects.create(id=id,user_id=i['userId'],title=i['title'],body=i['body']).save()

        post = Post.objects.filter(id=id)

    serializer = PostSerializer(post, many=True,context=serializer_context)

    if list(serializer.data) != []:
        return Response(serializer.data)
    else:
        return Response({"message":"This post does not exist."},status=status.HTTP_404_NOT_FOUND)



@api_view(["POST","GET"])
def post_create(request):
    if request.method == "GET":
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
        
    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def post_update(request,id):

    post = get_object_or_404(Post,id=id)

    if request.method == 'GET':
        serializer = PostUpdateSerializer(post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostUpdateSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)