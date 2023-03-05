"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from social_distribution import views         

router = routers.DefaultRouter()     



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', views.PostViewSet.as_view(), name='posts'),
    path('api/posts', views.PostViewSet.as_view(), name='posts'),
    path('api/posts/<int:pk>', views.PostViewSet.as_view(), name='post'),
    path('api/posts/<int:pk>/', views.PostViewSet.as_view(), name='post'),
    path('login', views.LoginView.as_view(), name='login'),
    path('api/authors', views.AuthorViewSet.as_view(), name='author'),
    path('api/authors/<int:pk>', views.AuthorViewSet.as_view(), name='author'),
    path('api/friendrequest',views.FriendRequestViewSet.as_view(),name='friendRequest'),
    path('api/friendrequest/<int:pk>',views.FriendRequestViewSet.as_view(),name='friendReq'),
    path('api/<int:pk>/friendrequest/<int:fk>',views.FriendRequestViewSet.as_view(),name='friendReq'),
    path('api/authors/<int:fk>/followers/<int:pk>',views.FollowersViewSet.as_view(),name='followers'),
    path('api/authors/<int:pk>/followers/',views.FollowersViewSet.as_view(),name='followers'),  
    path('service/authors', views.authors, name='authors'),
    path('service/authors/<str:author_id>', views.authors, name='author'),
    path('service/authors/<str:author_id>/followers', views.followers, name='followers'),
    path('service/authors/<str:author_id>/friends', views.friends, name='friends'),
    path('service/authors/<str:author_id>/posts', views.posts, name='posts'),
    path('service/authors/<str:author_id>/posts/<str:post_id>', views.posts, name='posts'),
    path('service/authors/<str:author_id>/posts/<str:post_id>/comments', views.comments, name='comments'),
    path('service/authors/<str:author_id>/inbox', views.inbox, name='inbox'),
    path('service/authors/<str:author_id>/liked', views.likedPosts, name='liked'),
    path('api/inbox/', views.InboxViewSet.as_view(), name='inbox'),
    path('api/home/', views.HomeViewSet.as_view(), name='home'),
    path('login', views.LoginView.as_view(), name='login')
]
