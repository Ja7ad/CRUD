from core.models import Category, Ad, User
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username')
        extra_kwargs = {
            'url': {'view_name': 'ads_by_user', 'lookup_field': 'pk'}
        }

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name',
            'email', 'username', 'password',
        )
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name')
        read_only_fields = ('id',)
        extra_kwargs = {
            'url': {'view_name': 'ads_by_category', 'lookup_field': 'pk'},
        }


class AdSerializer(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(read_only=True)
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Ad
        fields = (
            'id', 'url', 'title', 'image', 'description', 'price',
            'tell', 'address', 'category', 'owner','created', 'update'
        )
        extra_kwargs = {
            'url': {'view_name': 'ad_detail', 'lookup_field': 'pk'}
        }

class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = (
            'id', 'title', 'image', 'description','price',
            'tell', 'address', 'category', 'owner'
        )
        read_only_fields = ('id', 'owner')