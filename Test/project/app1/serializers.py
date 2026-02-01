from rest_framework import serializers
from .models import user_dashboard_table

class user_dashboard_table_serializer(serializers.ModelSerializer):
	class Meta:
		model=user_dashboard_table
		fields="__all__"
	