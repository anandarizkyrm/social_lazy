

from django.urls import path
from . import views

urlpatterns = [
    path('signin/', views.signinPage, name='login'),
    path('signup/', views.signupPage, name='register'),
    path('post/<str:id>/', views.detailPostPage, name="detail-post"),
    path('create/', views.createPage, name="create-post"),
    path('edit/<str:id>', views.editPage, name="edit-post"),
    path('comment-on-post/<str:id>/',
         views.createCommentOnPost, name="comment-on-post"),
    path('reply-comment/<str:id>/<str:post_id>/',
         views.ReplyToComment, name="reply-comment"),
    # path('post-like/<str:id>/', views.detailPostPage, name="detail-post"),

    path('', views.homePage, name='home'),


]
