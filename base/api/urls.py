from django.urls import path
from . import views

urlpatterns = [
    path('get-user-posts/<str:id>/', views.getUserPosts),
    path('post/', views.createPost),

    # path('rooms/<str:pk>/', views.getRoom),
]
