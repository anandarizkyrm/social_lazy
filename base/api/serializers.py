from rest_framework.serializers import ModelSerializer, IntegerField
from base.models import Post, Comment, CommentReply
from rest_framework import serializers


class CommentReplySerialize(ModelSerializer):
    class Meta:
        model = CommentReply
        fields = '__all__'


class CommentSerialize(ModelSerializer):
    comment_reply = CommentReplySerialize(many=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializers(ModelSerializer):
    total_comments = IntegerField(read_only=True)
    text = serializers.CharField(required=True)
    comments = CommentSerialize(many=True)

    class Meta:
        model = Post
        fields = '__all__'
