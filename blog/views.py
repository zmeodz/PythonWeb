from django.shortcuts import render
from .models import Post
# Create your views here.
def list(request):
    Data =  {'Post': Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', Data)