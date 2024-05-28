from django.db import models
from django.contrib.auth.models import User

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username
# Create your models here.





## decorator is a wrapper of a function, func is the w

# def my_decorator(function_we_are_wrapping):
#     def wrapper():
#         print('something is happening before the function is callled')
#         function_we_are_wrapping()
#         print('something is happing after the function is called')
#     return wrapper

# @my_decorator
# def say_hello():
#     print('hello')

# say_hello()

