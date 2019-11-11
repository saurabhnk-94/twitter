from rest_framework import serializers
from .models import *

class TweetUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = TweetUser
        fields = ('id', 'user_name','email_id')
        

class TweetSerializers(serializers.ModelSerializer):
    # user = TweetUserSerializers()
    class Meta:
        model = Tweet
        fields = ('id', 'user', 'tweet_box','date_created', 'date_updated','is_deleted')
        
        
class TweetSoftSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('is_deleted',)