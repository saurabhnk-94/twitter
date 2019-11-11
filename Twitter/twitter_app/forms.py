from django import forms
from .models import User, Tweet

class UserAdminForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super(UserAdminForm, self).__init__(*args)
        if not self.instance.id:
            self.fields['is_deleted'] = True
        else:
            self.fields['user_name'] = True
            self.fields['email_id'] = True
            
            
class TweetAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TweetAdminForm, self).__init__(*args)
        if not self.instance.id:
            self.fields['is_deleted'] = True
        else:
            self.fields['user'] = True
            self.fields['date_created'] = True
       