from django.db import models

# Create your models here.
class login_table(models.Model):
	email=models.EmailField(null=False)
	password=models.SlugField(max_length=6,null=False)
	def __str__(self):
		return self.email


