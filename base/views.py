from django.shortcuts import render, redirect
from .models import customUser, Post, Comment
from .forms import PostForm, RegisterForm, EditUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

@login_required(login_url= 'loginuser')
def home(request):
    q= request.GET.get('q') if request.GET.get('q') != None else ''
    posts= Post.objects.filter(Q(text__icontains= q) |
                               Q(user__username__icontains= q) ).order_by('-created')
    context= {'posts': posts}
    return render(request, 'base/home.html', context)


@login_required(login_url= 'loginuser')
def addpost(request):
    form= PostForm()
    if request.method== 'POST':
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            post= form.save(commit= False)
            post.user= request.user
            post.save()
            return redirect('home')
    context= {'form': form}
    return render(request, 'base/addpost.html', context)


def loginuser(request):
    page= 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method== 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')

        try:
            user= customUser.objects.get(username= username)
        except:
            messages.error(request, 'user does not exist')

        user= authenticate(request, username= username, password= password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'username OR password is wrong')

    return render(request, 'base/loginregister.html', {'page': page})


def logoutuser(request):
    logout(request)
    return redirect('home')


def registeruser(request):
    form= RegisterForm()

    if request.method== 'POST':
        form= RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user= form.save(commit= False)
            user.username= user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'an error occured during registration')

    return render(request, 'base/loginregister.html', {'form': form})


@login_required(login_url= 'loginuser')
def editpost(request, pk):
    mypost= Post.objects.get(id= pk)
    form= PostForm(instance= mypost)

    if request.user != mypost.user:
        return HttpResponse('You are not allowed here')

    if request.method== 'POST':
        form= PostForm(request.POST, request.FILES, instance= mypost)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'base/editpost.html', {'form': form})


@login_required(login_url= 'loginuser')
def deletepost(request, pk):
    mypost= Post.objects.get(id= pk)

    if request.user != mypost.user:
        return HttpResponse('You are not allowed here!')

    if request.method== 'POST':
        mypost.delete()
        return redirect('home')
    
    return render(request, 'base/deletepost.html', {'obj': mypost})


@login_required(login_url= 'loginPage')
def userpage(request, pk):
    users= customUser.objects.get(id= pk)
    myposts= users.post_set.all().order_by('-created')
    return render(request, 'base/userpage.html', {'myposts': myposts, 'users': users})


@login_required(login_url= 'loginPage')
def edituser(request):
    user= request.user
    form= EditUserForm(instance= user)
    if request.method== 'POST':
        form= EditUserForm(request.POST, request.FILES, instance= user)
        if form.is_valid():
            form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'base/edituser.html', {'form': form})


@login_required(login_url= 'loginPage')
def comment(request, pk):
    myPost= Post.objects.get(id= pk)
    comments= myPost.comment_set.all().order_by('-created')

    if request.method== 'POST':
        Comment.objects.create(
            user= request.user,
            post= myPost,
            text= request.POST.get('text')
        )
    context= {'comments': comments, 'myPost': myPost}
    return render(request, 'base/comment.html', context)


@login_required(login_url= 'loginPage')
def toggleLike(request, pk):
    post= Post.objects.get(id= pk)
    user= request.user

    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('home')


@login_required(login_url= 'loginuser')
def deletecomment(request, pk):
    mycommnet= Comment.objects.get(id= pk)

    if request.user != mycommnet.user:
        return HttpResponse('You are not allowed here!')

    if request.method== 'POST':
        mycommnet.delete()
        return redirect('home')
    
    return render(request, 'base/deletepost.html', {'obj': mycommnet})