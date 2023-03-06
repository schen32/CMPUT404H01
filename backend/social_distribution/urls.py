
from django.urls import path, include
from rest_framework import routers
from social_distribution import views 

router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like', views.LikeViewSet.as_view({'post' : 'like'}), name='post-likes'),
    path('users/', views.UserProfileListCreateView.as_view()),
    path('users/<int:id>/', views.UserProfileRetrieveUpdateView.as_view()),
    
]