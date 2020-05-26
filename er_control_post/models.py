from django.db import models
from django.conf import settings
from django.urls import reverse
class post(models.Model):
	user    = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
	company = models.CharField(max_length=150)
	job_title   = models.CharField(max_length=150)
	requirements = models.TextField()
	content = models.TextField()
	puplish = models.DateTimeField(auto_now=False,auto_now_add=True)
	update  = models.DateTimeField(auto_now=True,auto_now_add=False)
	contact = models.EmailField()

	def get_url(self):
		return reverse('detail',kwargs={'id':self.id})

	# def get_edit(self):
	# 	return reverse('update',kwargs={'id':self.id})

	def get_del(self):
		return reverse('delete',kwargs={'id':self.id})

