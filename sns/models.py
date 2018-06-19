from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, \
		related_name='group_owner')
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title
		
