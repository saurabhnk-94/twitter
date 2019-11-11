from django.urls import path
from .views import *


app_name = 'twitter_app'

urlpatterns = [
    path('user', api_get_all_user_list, name='user-list'),
    path('user/<int:id>', api_get_user_detail_view, name='user-details'),
    path('tweet', api_get_all_tweet_list, name='tweet-list'),
    path('tweet/<int:id>', api_get_tweet_detail_view, name='tweet-details'),
    path('user/create',api_create_user,name='create-user'),
    path('tweet/create',api_create_tweet,name='create-tweet'),
    path('tweet/<int:id>/update',api_update_tweet,name='update-tweet'),
]
