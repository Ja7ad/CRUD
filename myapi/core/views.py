from django.shortcuts import get_object_or_404

from core import serializers
from core.models import User, Category, Ad
from core.permissions import IsOwnerOrReadOnly

from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.authtoken.models import Token




class Root(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        content = {
            'ad_list': reverse('ad_list', request=request),
            'category_list': reverse('category_list', request=request),
            'user_list': reverse('user_list', request=request)
        }
        return Response(content)


class Signup(APIView):
    def post(self, request):
        serializer = serializers.UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            token = Token.objects.create(user=new_user).key
            content = {
                'user': serializer.data,
                'token': token
            }
            return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AdList(generics.ListCreateAPIView):    
    queryset = Ad.objects.all().order_by('-created')
    serializer_class = serializers.AdSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return serializers.AdCreateSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class AdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = serializers.AdSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return serializers.AdCreateSerializer
        return self.serializer_class


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    permission_classes = (permissions.IsAuthenticated,)


class AdsByCategory(generics.ListAPIView):
    queryset = Ad.objects.all().order_by('-created')
    serializer_class = serializers.AdSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return self.queryset.filter(category=category)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AdsByUser(generics.ListAPIView):
    queryset = Ad.objects.all().order_by('-created')
    serializer_class = serializers.AdSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        return self.queryset.filter(owner=user)
