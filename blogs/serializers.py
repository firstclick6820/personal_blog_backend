from .models import Post, Category, Comment
from rest_framework import serializers









class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'slug']
        
        
        
        
        


class PostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='slug'
    )

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'author', 'exerpt', 'body', 'created_at', 'updated_at', 'category', 'image']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        base_url = self.context['request'].build_absolute_uri('/')
        data['image_url'] = f'{base_url}{instance.image.url}'
        return data


        
        
        



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [ 'name', 'email' , 'message']
        required_fields = []  # Make the post field not required
