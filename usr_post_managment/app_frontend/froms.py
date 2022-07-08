from pyexpat import model
from django.forms import ModelForm, TextInput,Textarea
from app.models import Post

class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['user_id','title','body']
        widgets = {
            'user_id':TextInput(attrs={'class':'form-control'}),
            'title':TextInput(attrs={'class':'form-control'}),
            'body':Textarea(attrs={'class':'form-control'}),
        }