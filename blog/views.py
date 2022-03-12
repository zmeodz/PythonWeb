from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
# from .models import Post
# from django.views.generic import ListView, DetailView
# # Create your views here.
# # def list(request):
# #     Data =  {'Posts': Post.objects.all().order_by("-date")}
# #     return render(request, 'blog/blog.html', Data)
# class PostListView(ListView):
    # queryset = Post.objects.all().order_by("-date")
    # template_name = 'blog/blog.html'
    # context_object_name = 'Posts'
    # paginate_by = 10
# def post(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'blog/post.html', {'post': post})
# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post.html'
# def post(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404("Bài viết không tồn tại")
#     return render(request, 'blog/post.html', {'post': post})

def post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user,post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post":post, "form":form})