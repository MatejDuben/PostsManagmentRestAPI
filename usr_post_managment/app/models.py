from django.db import models
from django.forms import ValidationError
import requests


# Create your models here.
class Post(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=500)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"obj: {self.title}"


    def save(self, *args, **kwargs):
        user_exists = False
        users_api = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(users_api)
        data = response.json()
        for i in data:
            if int(self.user_id) == int(i['id']):
                user_exists = True
        if user_exists:
            print("Saved")
            super(Post, self).save(*args, **kwargs)
        else:
            print("No savee")
            raise ValidationError("User not found")
    