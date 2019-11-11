from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name','email_id')
        

class TweetSerializers(serializers.ModelSerializer):
    user = UserSerializers()
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'tweet_box', 'date_updated')