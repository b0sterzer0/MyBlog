from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, models
from django.http import HttpResponseRedirect
from .models import ProfileModel
from .forms import ProfileForm, LoginForm, RegisterForm
from app_blog.models import PostModel
from django.contrib.auth.views import LogoutView


def user_registration_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            ProfileModel.objects.create(
                user=user,
                city=form.cleaned_data['city'],
                date_of_birth=form.cleaned_data['date_of_birth']
            )

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/blog/wall/')
        return render(request, 'user/registration.html', context={'form': form})

    elif request.method == "GET":
        form = RegisterForm()
        return render(request, 'user/registration.html', context={'form': form})


def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user = models.User.objects.get(id=request.user.id)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.save()

            profile = ProfileModel.objects.get(user=request.user)
            profile.city = form.cleaned_data['city']
            profile.date_of_birth = form.cleaned_data['date_of_birth']
            profile.hobby = form.cleaned_data['hobby']
            profile.save()
            return HttpResponseRedirect('/user/profile/')
        return render(request, 'user/profile.html', context={'form': form})

    elif request.method == "GET":
        if request.user.is_authenticated:
            data = ProfileModel.objects.select_related('user').get(user=request.user)
            form = ProfileForm(initial={
                'first_name': data.user.first_name,
                'last_name': data.user.last_name,
                'email': data.user.email,
                'city': data.city,
                'date_of_birth': data.date_of_birth,
                'hobby': data.hobby
            })
            posts = PostModel.objects.filter(author=request.user)
            return render(request, 'user/profile.html', context={'form': form, 'posts': posts})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/blog/wall/')
        return render(request, 'auth/login.html', context={'form': form})
    elif request.method == "GET":
        form = LoginForm()
        return render(request, 'auth/login.html', context={'form': form})


class MyLogoutView(LogoutView):
    next_page = '/user/login/'
