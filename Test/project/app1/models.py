from django.db import models

class problem_table(models.Model):
	problem_id=models.SlugField(max_length=20,null=False,unique=True,primary_key=True)
	Problem_discription=models.TextField(null=True,blank=True)
	test_cases=models.FileField(upload_to="testcase/",null=False)

	def __str__ (self):
		return f"{self.problem_id}- {self.Problem_discription}"
	

class UserBoard(models.Model):
	email=models.EmailField(blank=False)
	problem=models.ForeignKey(problem_table, on_delete=models.CASCADE, blank=True, null=True,to_field=problem_table().problem_id ,related_name="userboards")
	has_done=models.BooleanField(default=False)
	language_used=models.CharField(max_length=20,default="----")
	time=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"email:{self.email}-- problem:{self.problem}---{self.language_used}--status:{self.has_done}---Time:{self.time}"


