from django.db import models
class testcase_table(models.Model):
	problem_id=models.SlugField(max_length=20,null=False,unique=True)
	discription=models.TextField(null=True,blank=True)
	test_cases=models.FileField(upload_to="testcase/")
	def __str__ (self):
		return self.problem_id
