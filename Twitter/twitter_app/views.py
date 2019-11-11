from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import User, Tweet
from .serializers import UserSerializers, TweetSerializers


@api_view(['GET',])
def api_get_all_user_list(request):
    user = User.objects.all()
    if request.method == 'GET':
        serializer = UserSerializers(user, many=True)
        return Response(serializer.data)
    

@api_view(['GET',])
def api_get_user_detail_view(request, id):
    try: 
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializers(user)
        return Response(serializer.data)


@api_view(['GET',])
def api_get_all_tweet_list(request):
    tweet = Tweet.objects.all()
    if request.method == 'GET':
        serializer = TweetSerializers(tweet, many=True)
        return Response(serializer.data)
    

@api_view(['GET',])
def api_get_tweet_detail_view(request, id):
    try: 
        tweet = Tweet.objects.get(id=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = UserSerializers(tweet)
        return Response(serializer.data)


