from django.urls import path
from .views import list_posts_view, create_post_view, detail_view, editing_post_view, delete_post_view
from .api import APIGetPostData, APIGetCommentData


urlpatterns = [
    path('wall/', list_posts_view, name='wall'),
    path('add/', create_post_view, name='add_post'),
    path('post/<int:post_id>/', detail_view, name='detail post view'),
    path('edit/<int:post_id>/', editing_post_view, name='edit post'),
    path('delete/<int:post_id>/', delete_post_view, name='delete post'),
    path('api/posts/', APIGetPostData.as_view(), name='api posts data'),
    path('api/comments/', APIGetCommentData.as_view(), name='api comments data'),
]
