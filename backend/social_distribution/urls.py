
from django.urls import path, include
from rest_framework import routers
from .views import LikeViewSet

router = routers.SimpleRouter()
routers.register(r'likes', LikeViewSet)

urlpatterns = [
    path('', include(router.urls))
]