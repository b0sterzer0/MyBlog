from django.shortcuts import render
from .models import PostModel, CommentModel
from .forms import CreatePostForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


def comment_add_view(request, post_id):
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            CommentModel.objects.create(
                author=request.user,
                text=form.cleaned_data['text'],
                post=PostModel.objects.get(id=post_id)
            )
        return HttpResponseRedirect(f'/blog/post/{post_id}/')


def create_post_view(request):
    """
    This func create a new post
    """
    if request.method == "POST":
        form = CreatePostForm(request.POST or None)
        if form.is_valid():
            post = PostModel(**form.cleaned_data)
            post.save()
            return HttpResponseRedirect('/blog/wall/')
        return render(request, 'blog/create_post.html', context={'form': form})
    elif request.method == "GET":
        form = CreatePostForm()
        return render(request, 'blog/create_post.html', context={'form': form})


def list_posts_view(request):
    """
    This func return all existing posts
    """
    if request.method == "POST":
        create_post_view(request)
        return HttpResponseRedirect('/blog/wall/')

    elif request.method == "GET":
        posts = PostModel.objects.select_related('author').all()
        form = CreatePostForm()
        return render(request, 'blog/list_post.html', context={'posts': posts, 'form': form})


def detail_view(request, post_id):
    """
    This func return post's data for detailed view
    """
    if request.method == "POST":
        comment_add_view(request, post_id)
        return HttpResponseRedirect(f'/blog/post/{post_id}/')

    elif request.method == "GET":
        try:
            post = PostModel.objects.get(id=post_id)
            comments = CommentModel.objects.filter(post=post)
            form = CommentForm()
            return render(request, 'blog/detail_view.html', context={'post': post, 'comment_form': form,
                                                                     'comments': comments})
        except ObjectDoesNotExist:
            return None


def editing_post_view(request, post_id):
    """
    This func for edit posts
    """
    if request.method == "POST":
        form = CreatePostForm(request.POST or None)
        if form.is_valid():
            post = PostModel.objects.get(id=post_id)
            post.title = form.cleaned_data['title']
            post.text = form.cleaned_data['text']
            post.save()
            return HttpResponseRedirect('/blog/wall/')
        return render(request, 'blog/edit_post.html', context={'form': form})

    elif request.method == "GET":
        posts = PostModel.objects.filter(id=post_id)
        if len(posts) == 1:
            post_data = posts[0]
            data = {
                'title': post_data.title,
                'author': post_data.author,
                'text': post_data.text,
                'add_date': post_data.add_date
            }
            form = CreatePostForm(initial=data)
            return render(request, 'blog/edit_post.html', context={'form': form})
        else:
            return HttpResponseRedirect('/blog/wall/')


def delete_post_view(request, post_id):
    """
    This func for delete post
    """
    post = PostModel.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/blog/wall/')
