from rest_framework import serializers
from .models import Post
import requests


class PostSerializer(serializers.ModelSerializer):
    url_detail = serializers.HyperlinkedIdentityField(view_name="post_detail",lookup_field="id")
    url_edit = serializers.HyperlinkedIdentityField(view_name="post_edit",lookup_field="id")
    class Meta:
        model=Post
        fields="__all__"

    def validate_user_id(self,value):       #kontroluje ci zadane user_id existue medzi users v externej api
        user_exists = False
        users_api = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(users_api)
        data = response.json()
        for i in data:
            if int(value) == int(i['id']):
                user_exists = True
        if not user_exists:
            raise serializers.ValidationError("User does not exist.")
        return value

class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=[
            "title",
            "body"
        ]