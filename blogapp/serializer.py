from rest_framework import serializers
from .models import Category,Post

class CategorySerializer(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    title=serializers.CharField(required=True,allow_blank=False,max_length=100)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.save()
        return instance
    

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields="__all__"