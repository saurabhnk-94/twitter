from django.urls import path
from .views import *


app_name = 'twitter_app'

urlpatterns = [
    path('user', api_get_all_user_list, name='user-list'),
    path('user/<id>', api_get_user_detail_view, name='user-details'),
    path('tweet', api_get_all_tweet_list, name='tweet-list'),
    path('tweet/<id>', api_get_tweet_detail_view, name='tweet-details')
]
