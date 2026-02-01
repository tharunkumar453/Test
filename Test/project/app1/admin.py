from django.contrib import admin
from .models import problem_table,user_dashboard_table
admin.site.register(problem_table)
admin.site.register(user_dashboard_table)