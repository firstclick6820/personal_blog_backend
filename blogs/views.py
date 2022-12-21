from django.shortcuts import render
from django.http import HttpResponse

from .serializers import PostSerializer, CategorySerializer, CommentSerializer
from .models import Post, Category, Comment
from django.shortcuts import get_object_or_404

from rest_framework import permissions



from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

def Home(request):
    return HttpResponse("Home page")


# List All The Categories
class CategoryListAPIView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get']
    
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True,context={'request': request} )
        return Response(serializer.data)



    def get_related_category_all_post(self, request, slug):
        
        # let's grap the category first
        category = Category.objects.filter(slug=slug).first()
        
        if category:
            
            # now let's grap all the posts in the category
            posts = category.post_set.all()
            serializer = PostSerializer(posts, many=True, context={'request': request})
            
            return Response(serializer.data)



# List All The Posts
class PostListAPIView(viewsets.ViewSet):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get']
    
    # Getting All The Posts
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)
    
    
    # Getting Recent Posts
    def get_recent_posts(self, request):
        recent_posts = Post.objects.all().order_by('-created_at')[:10]
        serializer = PostSerializer(recent_posts, many=True, context={'request': request})
        return Response(serializer.data)



    # Getting Specific category
    def get_related_posts(self,request , slug):
         # get the post
        post = get_object_or_404(Post, slug=slug)

        # get the related categories
        categories = post.category.all()

        # get the related posts
        posts = Post.objects.filter(category__in=categories).exclude(id=post.id)
        serializer = PostSerializer(posts, many=True, context={'request': request})

        return Response(serializer.data)


    # Getting Post Details For A Specific Slug requested
    def get_post_details(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer = PostSerializer(post, many=False, context={'request': request})
        return Response(serializer.data)
    
    


# Comment View
class CommentListView(viewsets.ViewSet):
    
    permission_classes = (permissions.AllowAny,)
    http_method_names = ['get', 'post']
    
    
    
  
    
    
    def get_post_related_comments(self, request, slug):
        # find the post
        post = Post.objects.filter(slug=slug).first()
        # check if the post is exist
        if post:
            # now grap all the comments in that post with a status of "published"
            comments = post.comments.filter(status='p')
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

        return Response('No Posts')

    
    
    
    
    
    def post_a_comment(self, request, slug):
        # Check if the request is a post request.
        if request.method == "POST":
            # Find the post.
            post = Post.objects.filter(slug=slug).first()
         
            

            # Serialize the comment data from the request.
            serializer = CommentSerializer(data=request.data)
          
            if serializer.is_valid():
                
                # Set the post field of the comment instance.
                comment = serializer.save(post=post)
                comment.save()
                return Response("Comment is submitted for review")
            return Response(serializer.errors)

            
            