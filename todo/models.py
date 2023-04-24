from django.db import models

# Create your models here.

class To_Do(models.Model):
	task = models.CharField(max_length=200)
	start_time = models.CharField(max_length=30)
	end_time = models.CharField(max_length=30)
	


	def __str__(self):
		return (f"<strong>{self.task}</strong> ' ' {self.start_time} ' ' {self.end_time} ")
