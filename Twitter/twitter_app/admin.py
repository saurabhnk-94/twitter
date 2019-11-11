from django.contrib import admin
from .models import TweetUser, Tweet

class TweetUserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email_id','is_deleted',)
    orderering = ('user_name',)
    search_fields = ['user_name']

admin.site.register(TweetUser, TweetUserAdmin) 

class TweetAdmin(admin.ModelAdmin):
    list_display = ('first_10_characters','user','tweet_box','date_created','date_updated','is_deleted')
    orderering = ('-date_updated',)
    search_fields = ['tweet_box','user']

admin.site.register(Tweet, TweetAdmin)