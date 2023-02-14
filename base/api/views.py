from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Post, Comment, CommentReply
from .serializers import PostSerializers
# from base.api import serializers
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Count
from rest_framework import status
# Create your views here.
from rest_framework.exceptions import ValidationError


@api_view(['GET'])
def getUserPosts(request, id):
    posts = Post.objects.filter(author_id=id).annotate(
        total_comments=Count('comment'),
        total_comment_replies=Count('comment__commentreply'),
    )
    serializer = PostSerializers(posts, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createPost(request):
    try:
        serializer = PostSerializers(data={
            "text": request.data.get("text"),
            "author": request.META["HTTP_USER"]
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
