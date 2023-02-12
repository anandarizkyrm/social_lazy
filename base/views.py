from django.shortcuts import render, redirect
from .models import User, Post, Comment, CommentReply
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm, PostForm
# Create your views here.
from django.db.models import Count


def homePage(request):
    posts = Post.objects.annotate(comment_count=Count('comment', distinct=True),
                                  reply_count=Count(
                                      'comment__commentreply', distinct=True),
                                  )
    return render(request, 'base/home.html', {"posts": posts})


def createPage(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/create.html', {'form': form})


def createCommentOnPost(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":

        Comment.objects.create(
            post_id=post,
            author_id=request.user,
            comment=request.POST.get('comment')
        )
        return redirect('detail-post', id)
    return redirect('home')


def ReplyToComment(request, id, post_id):

    comment = Comment.objects.get(id=id)

    if request.method == "POST":
        CommentReply.objects.create(
            comment_id=comment,
            author_id=request.user,
            reply=request.POST.get('reply')
        )
        return redirect('detail-post', post_id)
    return redirect('home')


def editPage(request):
    return render(request, 'base/create.html')


def detailPostPage(request, id):
    post = Post.objects.get(id=id)
    users_who_liked = post.likes.all()
    comments = Comment.objects.filter(post_id=id)

    # i  believe this query should be optimize in the future  T_T
    comment_reply_total = 0
    for comment in comments:
        comment_reply = CommentReply.objects.filter(comment_id=comment)
        comment_reply_total += comment_reply.count()

    total_comment_count = comments.count() + comment_reply_total

    context = {"post": post, "comments": comments,
               "likes": users_who_liked, "total_comment": total_comment_count}
    return render(request, 'base/detailpost.html', context)


def signinPage(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Credentials Invalid')

    return render(request, "signin.html")


def signupPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 and password is not "":
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=password)
                user.save()

                messages.success(
                    request, 'Account created successfully. Please log in to continue.')
                return redirect('login')
        else:
            messages.info(
                request, 'Password Not Valid Please Check Your Password')
            return redirect('register')

    else:
        return render(request, 'signup.html')
