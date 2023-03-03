from pstats import Stats
import statistics
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import PostSerializer, LoginSerializer, AuthorSerializer, CommentSerializer, CreatePostSerializer, LikeSerializer
from .models import Post, Author, Comment, Like
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


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

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    
    @api_view(['POST'])
    def like(self, request, pk):
        post_id = request.data.get('post_id')
        user = request.user
        if post_id and user.is_authenticated:
            like = Like.objects.create(post_id=post_id, user=user)
            likes_count = Like.objects.filter(post_id=post_id).count()
            return Response({'likes' : likes_count})
        return Response({'error' : 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
            
    

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
    
    


        





