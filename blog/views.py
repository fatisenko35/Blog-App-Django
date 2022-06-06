from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from blog.forms import BlogForm, CommentForm
from blog.models import BlogModel
from auth_.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
# Create your views here.
def home(request):
    return render(request, 'blog/home.html')


def blog_add(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')

    context = {
        'form': form,
    }
    return render(request, 'blog/blog_add.html', context)


def blog_list(request):
    blogs = BlogModel.objects.all()
    context = {'blogs':blogs}
    return render(request, 'blog/blog_list.html', context)

def blog_update(request, id):
    blog = BlogModel.objects.get(id=id)
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('list') 

    context = {
        'form': form,
        'blog': blog
        } 

    return render(request, 'blog/blog_update.html', context)               
def blog_details(request, id):
    blog_comment = get_object_or_404(BlogModel, id=id)
    comments = blog_comment.comments.filter(activate=True)
    comment_count = comments.count()
    liked = False
    if blog_comment.likes.filter(id=request.user.id).exists():
        liked = True
    likes_count = blog_comment.likes.count()    
    blog = BlogModel.objects.get(id=id)
    blog.view_count = blog.view_count + 1
    blog.save()
    context = {
        'blog': blog,
        'comments': comments,
        'comment_count': comment_count,
        'liked': liked,
        'likes_count': likes_count
        
        } 

    return render(request, 'blog/blog_details.html', context)               

def blog_delete(request, id):
    print("hi")
    blog = BlogModel.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('list')
    return render(request, 'blog/blog_delete.html', {'blog': blog})

 
def blog_comment(request, id):
    show = True
    blog = get_object_or_404(BlogModel, id=id)
    comments = blog.comments.filter(activate=True)
    comment_count = comments.count()
    liked = False
    if blog.likes.filter(id=request.user.id).exists():
        liked = True
    likes_count = blog.likes.count() 
    if request.method == 'POST':
        show = not show
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.blog = blog
            new_comment.activate = True
            new_comment.author = request.user
            new_comment.save()
            comment_count = comments.count()
            
            comments = blog.comments.filter(activate=True)
            return redirect('details', id=id)
    else:
        form = CommentForm()
        
    return render(request, 'blog/blog_details.html', {'form': form, 'comments': comments,'blog': blog, 'show': show, 'comment_count': comment_count, 'liked': liked, 'likes_count': likes_count})

def blog_post_like(request, id):
    post = get_object_or_404(BlogModel, id=id)
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
        return redirect('details', id=id)
    else:
        post.likes.add(request.user)
        liked = True
        return redirect('details', id=id)
    likes_count = post.likes.count()
    return render(request, 'blog/blog_details.html', {'blog': post, 'likes_count': likes_count})