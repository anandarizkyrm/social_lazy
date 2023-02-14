from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Post, Comment, CommentReply
from .serializers import PostSerializers
# from base.api import serializers
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.


@api_view(['GET'])
def getUserPosts(request, id):
    posts = Post.objects.filter(author_id=id).annotate(
        total_comments=Count('comment'),
        total_comment_replies=Count('comment__commentreply'),
    )
    serializer = PostSerializers(posts, many=True)

    return Response(serializer.data)
