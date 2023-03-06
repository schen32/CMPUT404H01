from pstats import Stats
import statistics
from django.shortcuts import (render, get_object_or_404)
from rest_framework import viewsets, status
from .serializers import PostSerializer, LoginSerializer, AuthorSerializer, CommentSerializer, CreatePostSerializer, LikeSerializer
from .models import Post, Author, Comment, Like
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, DestroyAPIView



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    @api_view(['GET'])
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    @api_view(['DELETE'])
    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(status="204")
    
    @api_view(['PUT'])
    def put(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = CreatePostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status="200")
        return Response(serializer.errors, status="400")
    
    @api_view(['POST'])
    def post(self, request):
        serializer = CreatePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status="201")
        return Response(serializer.errors, status="400")

class LikeViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        try:
            # create a new like if the user has not already liked the post
            like = Like.objects.create(post=post, user=user)
            post.count += 1
            post.save()
            serializer = PostSerializer(post)
            print(f"POST request to like post {pk} by user {user} succeeded.")
            return Response(serializer.data, status="201")
        except:
            # return a 400 error if the user has already liked the post
            return Response({'error': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        try:
            # delete the user's like if they have already liked the post
            like = Like.objects.get(post=post, user=user)
            like.delete()
            post.count -= 1
            post.save()
            serializer = PostSerializer(post)
            print(f"DELETE request to unlike post {pk} by user {user} succeeded.")
            return Response(serializer.data)
        except:
            # return a 400 error if the user has not already liked the post
            return Response({'error': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    
    @like.mapping.get
    def list(self, request, post_id=None):
        post = Post.objects.get(pk=post_id)
        likes = Like.objects.filter(post=post)
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        try:
            # delete the user's like if they have already liked the post
            like = Like.objects.get(post=post, user=user)
            like.delete()
            post.count -= 1
            post.save()
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except:
            # return a 400 error if the user has not already liked the post
            return Response({'error': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    

class LoginView(APIView):

    def post(self, request):
        try:
            data = LoginSerializer.validate(request.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)
    
    


        





