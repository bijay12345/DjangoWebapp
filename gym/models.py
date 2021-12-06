from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})


class Video(models.Model):
	context=models.CharField(max_length=100)
	video = models.FileField(upload_to='video/%y')
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.context

	def get_absolute_url(self):
		return reverse('video-detail',kwargs={'pk':self.pk})