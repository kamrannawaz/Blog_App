from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet,ViewSet
from .models import Category, Post
from .serializer import CategorySerializer, PostSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class GetAllCategory(APIView):
    def get(self,request):
        query = Category.objects.all()
        serializer = CategorySerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class GetCategory(APIView):
    def get(self,request,pk=None):
        if not pk:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
        try:
            query = Category.objects.get(id=pk)
            serializer = CategorySerializer(query)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
    
class CreateCategory(APIView):
    def post(self,request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response(category.data,status=status.HTTP_201_CREATED)
        return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateCategory(APIView):
    def put(self,request,pk=None):
        category_id = pk
        if not category_id:
            return Response({},status=status.HTTP_404_NOT_FOUND)
        try:
            query = Category.objects.get(id=category_id)
            category = CategorySerializer(query,data=request.data)
            if category.is_valid():
                category.save()
                return Response(category.data,status=status.HTTP_200_OK)
            return Response(category.errors, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
        
class DeleteCategory(APIView):
    def delete(self,request,pk=None):
        if not pk:
            return Response({},status=status.HTTP_404_NOT_FOUND)
        try:
            query = Category.objects.get(id=pk)
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
        

class PostViewSet(ViewSet):
    """
    A simple ViewSet for Post Model.
    """

    def list(self,request):
        query = Post.objects.all()
        serializer = PostSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def get(self,request,pk=None):
        if not pk:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
        try:
            query = Post.objects.get(id=pk)
            serializer = PostSerializer(query)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
    
    def create(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
    def update(self,request,pk=None):
        if not pk:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
        try:
            query = Post.objects.get(id=pk)
            serializer = PostSerializer(query,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
        
    def delete(self,request,pk=None):
        if not pk:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)
        try:
            query = Post.objects.get(id=pk)
            query.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message":"not found!"},status=status.HTTP_404_NOT_FOUND)