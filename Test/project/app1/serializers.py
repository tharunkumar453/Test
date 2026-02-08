from rest_framework import serializers
from .models import problem_table,UserBoard


class ProblemTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = problem_table
        fields = ['problem_id']


class UserDashboardSerializer(serializers.ModelSerializer):
  
    #problems=ProblemTableSerializer(many=True,read_only=True)
    class Meta:
        model = UserBoard
        fields = "__all__"
       