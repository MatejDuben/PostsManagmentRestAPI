from django.shortcuts import render, redirect
from app.models import Post
from .froms import CreatePostForm

def show_posts(request):
    return render(request,'index.html')

def create_post(request):
    form = CreatePostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('show_posts')

    return render(request,'create_post.html',{'form':form})

