# twitter-repo

Features:
1. A user can post tweets.
2. A tweet can have only 140 characters.
3. A tweet will have date and time of postings.
4. A tweet will have user associated.
5. Tweets will be fetched in descending order of posting.
6. All tweets are public, everyone can see all tweets.
7. A user has unique email address.
8. User has a name.
9. User can soft delete his tweet.
10. User can update his tweet.


About the project:
>> My project name is Twitter.
>> My app name is twitter_app.
>> There are 2 classes in my app-models: TweetUser and Tweet
>> TweetUser: It has attributes user_name,email_id and is_deleted(default=false).
>> Tweet: user as a foreign key, tweet_box for the tweet, date created, date_updated and is_deleted(default=false)
>> The ordering will be done through the updated date and time field.
>> Rest API is being used and in that we have used function based view.

Summary:
Language: Python - version(3.6.8)
Framework: Django - version(2.2.7)

