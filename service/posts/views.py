from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Rating, Comment
from .forms import PostForm, CommentForm, RatingForm
from django.db.models import Avg
from django.views.generic import ListView


@login_required
def post_list(request):
    posts = Post.objects.all()
    post_rating = Rating.objects.values_list('post_id').annotate(avg_rating=Avg('rating'))
    context = {
        'posts': posts,
        'post_rating': post_rating
    }
    return render(request, 'post_list.html', context)




@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('posts:post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:post_list')

@login_required
def add_comment_to_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:add_rating_to_post', pk=post.pk)
        else:
            return redirect('posts:post_list')
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})

@login_required
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = post.comments.all()
    comment = Comment.objects.filter(post=post)
    ratings = Rating.objects.filter(post=post).all()
    rating = ratings.values_list('rating')
    average_rating = ratings.aggregate(Avg('rating'))['rating__avg']
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('posts:post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'form': form, 'ratings': ratings, 'average_rating': average_rating, 'rating': rating})


@login_required
def add_rating_to_post(request, pk, *args,**kwargs):
    post = Post.objects.get(pk=pk)
    comment = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.post = post
            rating.user = request.user
            rating.comments_id = comment.values_list('id').last()[0]
            rating.save()
            return redirect('posts:post_detail', pk=post.pk)
        else:
            return redirect('posts:post_list')
    else:
        form = RatingForm()
    return render(request, 'add_rating_to_post.html', {'form': form})


class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(school_name__icontains=query)
        return (object_list)