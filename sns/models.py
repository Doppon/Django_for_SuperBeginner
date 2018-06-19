from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, \
		related_name='group_owner')
	title = models.CharField(max_length=100)

	def __str__(self):
		return self.title


class Friend(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, \
		related_name='friend_owner')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	group = models.ForeignKey(Group, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.user) + '(group"' + str(self.group) + '")'


class Good(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE, \
		related_name='good_owner')
	message = models.ForeignKey(Message, on_delete=models.CASCADE)

	def __str__(self):
		return 'good for "' + str(self.message) + '" (by ' + \
			str(self.owner) + ')'
			
