from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50)
    mail_id =models.EmailField()

    def __str__(self):
        return self.user_name
    

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models






