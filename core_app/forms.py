from django.contrib.auth.forms import UserCreationForm
from .models import User

# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1', 'password2']
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password1'].help_text = ''
#         self.fields['password2'].help_text = '' 
#         self.fields['username'].help_text = '' 
    