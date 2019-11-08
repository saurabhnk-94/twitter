from django.test import TestCase
from .models import User, Tweet


class UserTest(TestCase):
    def setUp(self):
        """
        To check whether my database gets created
        """
        user1 = User.objects.create(user_name='Saurabh', email_id='saurabhnk94@gmail.com')
        user2 = User.objects.create(user_name='Venkatesh', email_id='sean@gmail.com')
    
    
    def test_case_get_username_email(self):
        '''
        To get user email 
        '''
        user_info = User.objects.get(user_name='Saurabh')
        self.assertEqual(user_info.username_email(), 'saurabhnk94@gmail.com')


class TweetTest(TestCase):
    def setUp(self):
        '''
        Making the tweet class test
        '''
        user1 = User.objects.create(user_name='Saurabh', email_id='saurabhnk94@gmail.com')
        tweet_user = User.objects.get(user_name='Saurabh')
        Tweet.objects.create(user=tweet_user,tweet_box='Hello everyone!!! This is a Twitter test box')

    
    def test_case_get_tweet(self):
        tweet_user = User.objects.get(user_name='Saurabh')
        tweet_char = Tweet.objects.get(user=tweet_user)
        self.assertEqual(tweet_char.first_10_characters(),'Hello ever...')
    
    