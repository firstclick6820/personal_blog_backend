from django.http import HttpResponse
from django.urls import path

from .views import Home, CategoryListAPIView, PostListAPIView, CommentListView


urlpatterns = [
    path('', Home, name="HomePage" ),
    path('posts/', PostListAPIView.as_view({'get': 'get'}), name='post_list'),
    path('recent_posts/',PostListAPIView.as_view({'get': 'get_recent_posts'})),
    path('get_related_posts/<slug:slug>/', PostListAPIView.as_view({'get': 'get_related_posts'})),
    path('post_details/<slug:slug>/',PostListAPIView.as_view({'get': 'get_post_details'}) ),
    path('categories/', CategoryListAPIView.as_view({'get': 'get'}), name='category_list'),
    path('categroies/<slug:slug>/', CategoryListAPIView.as_view({'get': 'get_related_category_all_post'})),
    path('get_post_related_comments/<slug:slug>/', CommentListView.as_view({'get': 'get_post_related_comments'})),
    path('<slug:slug>/comment/', CommentListView.as_view({'post': 'post_a_comment'}))
    
    
]
