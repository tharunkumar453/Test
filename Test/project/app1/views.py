from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import problem_table

import json
from app1.CombindCode import PythonCombiner,CppCombiner
from app1.code_exicution import code_execution_python,code_execution_cpp
class submit(APIView):
  
    parser_classes = [MultiPartParser]

    def post(self, request):
        user_email=request.data.get("user_email")
        user_name=request.data.get("user_name")
        name=request.data.get("name")
        submission_id=request.data.get("submission_id")
        file=request.FILES["file"].read().decode("utf-8")
        problem_id=request.data.get("problem_id")
        language=request.data.get("language")
        test_case_file=problem_table.objects.get(problem_id=problem_id)
        with test_case_file.test_cases.open("r") as j:
            tc=json.load(j)
        if language=="python":
            combined_code=PythonCombiner.combined_file_python(file,tc) 
            output_from_subprocess=code_execution_python().execute_code(combined_code,name)
            return Response(output_from_subprocess)

        if language=="cpp":
            combined_code=CppCombiner.combined_file_cpp(file,tc) 
          
                
                
            return Response(code_execution_cpp().execute_code(combined_code,name))
        

class userDashboard(APIView):
    def get(self,request):
        user_email=request.data.get("user_email")
        try:
            dashboard_data=user_dashboard_table.objects.get(user_EmailD=user_email)
            serializer=user_dashboard_table_serializer(dashboard_data)
            return Response(serializer.data)
        except user_dashboard_table.DoesNotExist:
            return Response({"error":"User dashboard not found"},status=404)