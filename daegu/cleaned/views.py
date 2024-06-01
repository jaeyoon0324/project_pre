from django.shortcuts import render
from search.models import Post

def cleaned_posts_list(request):
    posts = Post.objects.using('cleaned').all()
    return render(request, 'cleaned_posts_list.html', {'posts': posts})
