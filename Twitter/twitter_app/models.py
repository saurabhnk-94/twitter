from django.db import models


class TweetUser(models.Model):
    user_name = models.CharField(max_length=50,unique=True)
    email_id =models.EmailField(unique=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name
    
    def username_email(self):
        return self.email_id
    

class Tweet(models.Model):
    user = models.ForeignKey(TweetUser, on_delete=models.CASCADE)
    tweet_box = models.TextField(max_length=140)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
   
    
    def __str__(self):
        return self.tweet_box
    
    def first_10_characters(self):
        return self.tweet_box[:10]+'...'
 
    
    
    
    






