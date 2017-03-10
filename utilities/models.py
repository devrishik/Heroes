from __future__ import unicode_literals

from django.db import models


class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	class Meta:
		abstract = True


class Token(TimeStampedModel):
	token = models.CharField(max_length=255, unique=True)

	def __str__(self):
		return self.token
