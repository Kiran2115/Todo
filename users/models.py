from django.db import models
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
# 	pass

class User(AbstractUser):
	# user_id = models.IntegerField(


	# username = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)


    
	class Meta:
    		ordering =('email',)

	def __str__(self):
    		return self.username
