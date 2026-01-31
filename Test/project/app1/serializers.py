from dataclasses import fields
from rest_framework import serializers
from .models import testcase_table

class test_case_serializer(serializers.ModelSerializer):
	class Meta:
		model=testcase_table
		fields="__all__"
	