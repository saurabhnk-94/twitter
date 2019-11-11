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


@api_view(['POST'])
def api_create_user(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Created Successfully'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data['failure'] = 'Creation Unsuccessful'
            return Response(data, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def api_create_tweet(request):
    if request.method == 'POST':
        serializer = TweetSerializers(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Created Successfully'
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data['failure'] = 'Creation Unsuccessful'
            return Response(data, status=status.HTTP_404_NOT_FOUND)



@api_view(['PUT'])
def api_update_tweet(request, id):
    try:
        tweet = Tweet.objects.get(id=id)
    except Tweet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  
    if request.method == 'PUT':
        serializer = TweetSerializers(tweet)
        if serializer.is_valid():
            data = {}
            serializer.save()
            data['success'] = "Update Successful"
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)       
