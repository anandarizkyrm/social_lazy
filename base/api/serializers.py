from rest_framework.serializers import ModelSerializer, IntegerField
from base.models import Post, Comment, CommentReply


class PostSerializers(ModelSerializer):
    total_comments = IntegerField(read_only=True)
    total_comment_replies = IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerialize(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CommentReplySerialize(ModelSerializer):
    class Meta:
        model = CommentReply
        fields = '__all__'
