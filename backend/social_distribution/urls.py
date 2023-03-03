
from django.urls import path, include
from rest_framework import routers
from .views import LikeViewSet, CommentViewSet

router = routers.SimpleRouter()
routers.register(r'likes', LikeViewSet)
routers.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]