from django.shortcuts import render
from apiapp.serializers import PostSerializer
from mainapp.models import Post
from rest_framework.views import APIView,Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly,IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer    

# class PostListAPIView(generics.ListCreateAPIView):
#     permission_classes = [
#         IsAuthenticatedOrReadOnly,    
#     ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [
#         IsAuthorOrReadOnly,
#     ]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
    
# class PostDeleteAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostListView(APIView):
#     def get(self,request):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts,many=True)
#         return Response(serializer.data)

    
# class PosrCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer