from token import CIRCUMFLEX

from django.contrib.admin.templatetags.admin_list import ResultList
from django.core.serializers import serialize
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import PostSerializer, PostPointSerializer, CommentSerializer
from ..models import Post, PostPoint, Comments
from rest_framework.decorators import api_view

from ..views import post_point_edit



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostPointViewsSet(viewsets.ModelViewSet):
    queryset = PostPoint.objects.all()
    serializer_class =  PostPointSerializer

@api_view(['GET'])
def post_list(request):
    objects = Post.objects.all()
    serialize_class = PostSerializer(objects, many=True)
    return Response(serialize_class.data)

@api_view(['GET'])
def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    post_serializer = PostSerializer(post)
    post_points = PostPoint.objects.filter(post=post)
    post_point_serializer = PostPointSerializer(post_points, many=True)
    comments = Comments.objects.filter(post=post)
    comments_serializer = CommentSerializer(post_points, many=True)

    return Response({'post':post_serializer.data,
                     'post_points' :post_point_serializer.data,
                     'comments': comments_serializer.data})


@api_view(['POST'])
def post_create(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def post_point_create(request):
    serializer = PostPointSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def comment_create(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def post_update(request, pk):
    post = Post.objects.get(id=pk)
    serializer = PostSerializer(data=request.data, instance=post)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def post_point_update(request, pk):
    post_point = PostPoint.objects.get(id=pk)
    serializer = PostPointSerializer(data=request.data, instance=post_point )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def comment_update(request, pk):
    comment = Comments.objects.get(id=pk)
    serializer = CommentSerializer(data=request.data, instance=comment)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def comment_delete(request, pk):
    comment = Comments.objects.get(id=pk)
    comment.delete()
    return JsonResponse({'delete, status': status.HTTP_204_NO_CONTENT})

@api_view(['DELETE'])
def post_point_delete(request, pk):
    post_point = PostPoint.objects.get(id=pk)
    post_point.delete()
    return JsonResponse({'delete, status': status.HTTP_204_NO_CONTENT})

@api_view(['DELETE'])
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return JsonResponse({'delete, status': status.HTTP_204_NO_CONTENT})