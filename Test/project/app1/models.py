from django.db import models
class problem_table(models.Model):
	problem_id=models.SlugField(max_length=20,null=False,unique=True)
	discription=models.TextField(null=True,blank=True)
	test_cases=models.FileField(upload_to="testcase/")

	def __str__ (self):
		return self.problem_id


class problem_submission_table(models.Model):
	submission_id=models.AutoField(primary_key=True)
	user_id=models.SlugField(max_length=20,null=False)
	problem_id=models.SlugField(max_length=20,null=False)
	code_file=models.FileField(upload_to="user_code/")
	language_used=models.CharField(max_length=30,null=False)
	submission_time=models.DateTimeField(auto_now_add=True)
	toal_problems_solved=models.IntegerField(default=0)

	def __str__ (self):
		return f"Submission {self.toal_problems_solved} by User {self.user_id} for Problem {self.problem_id}"
	
class user_dashboard_table(models.Model):
	user_name=models.CharField(max_length=50,null=False)
	user_EmailD=models.EmailField(max_length=50,null=False,unique=True)
	total_submissions=models.IntegerField(default=0)
	problems_solved=models.IntegerField(default=0)

	def __str__ (self):
		return f"Dashboard for User {self.user_EmailD}"