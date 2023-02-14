from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True)

    likes = models.ManyToManyField(
        User, related_name="liked_posts", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def comments_count(self):
        return self.likes.count()

    def __str__(self):
        return self.text


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


class CommentReply(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    reply = models.TextField(max_length=200)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    comment_id = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=False)
    # post_id = models.ForeignKey(
    #     Post, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.reply
