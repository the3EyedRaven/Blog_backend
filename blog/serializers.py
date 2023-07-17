from rest_framework import serializers
from .models import Category, Blog

class ModalBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id','title','desc','cover','date']

class CategorySerializer(serializers.ModelSerializer):
    blogs = ModalBlogSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','category','title','cover','blogs']



class ModalCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

# class ModalAuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = ['name']

class BlogSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field='category', read_only=True)
    # author = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)
    category = ModalCategorySerializer(read_only=True)
    # author = ModalAuthorSerializer(many=True, read_only=True)
    
    class Meta:
        model = Blog
        fields = ['id','title','desc','cover','date','category']



# class AuthorSerializer(serializers.ModelSerializer):
#     blogs = ModalBlogSerializer(many=True, read_only=True)
#     class Meta:
#         model = Author
#         fields = ['id','name','biography','date_of_birth','blogs']

