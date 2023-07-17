# Create your views here.
from .models import Blog, Category
from .serializers import BlogSerializer, CategorySerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

# class BlogViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Blog.objects.all()
#         serializer = BlogSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Blog.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = BlogSerializer(user, context={'request': request})
#         return Response(serializer.data)

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    queryset = Blog.objects.order_by('-date')
    serializer_class = BlogSerializer
    paginator = None


class CreateBlogAPIView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    queryset = Blog.objects.order_by('-date')
    serializer_class = BlogSerializer
    paginator = None

    def perform_create(self, serializer):
        post = serializer.save()
        print(post)
        # Set category
        try:
            cate = self.request.data['category']
            print(type(cate))
        except:
            cate = ""        
        if cate:
            # cat = Category.objects.all(category)
            # print(type(cat))
            # print(cat)
            category = Category.objects.get(category=cate)
            print(type(category))
            print(category)
            post.category = category
        else:
            print("wrong category")
        
        # # Add author
        # try:
        #     author_string = self.request.data['author']
        # except:
        #     author_string = ""
        # if author_string:
        #     post = add_author(post, author_string)

        post.save()
    

class CategoryViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        paginator = None
        
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = Category.objects.all()
        category = kwargs.get('category',None)
        category = Category.objects.get(category=category)
        serializer = CategorySerializer(category, context={'request': request})
        paginator = None
        return Response(serializer.data)
    

# class AuthorViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Author.objects.all()
#         serializer = AuthorSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Author.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = AuthorSerializer(user)
#         return Response(serializer.data)

# class AuthorViewSet(viewsets.ModelViewSet):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer