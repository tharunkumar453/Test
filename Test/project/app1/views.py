from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import problem_table

from app1.MiddleWare import DriverCodeMiddleware,ExecuteCodeFactory
from app1.workers import WriteInFile
class submit(APIView):
  
    parser_classes = [MultiPartParser]

    def post(self, request):
        user_email=request.data.get("user_email")
        user_name=request.data.get("user_name")
        name=request.data.get("name")
        submission_id=request.data.get("submission_id")
        user_codefile=request.FILES["file"].read().decode("utf-8")
        problem_id=request.data.get("problem_id")
        language=request.data.get("language")
        test_case_file=problem_table.objects.get(problem_id=problem_id)



        testcaseJson=WriteInFile.write_in_file(test_case_file)
        output_handler=ExecutionHandler().handle_execution(language,user_codefile,testcaseJson,name)



        code_output={
            "message":output_handler["message"],
            "filename":output_handler["filename"],
            "output":output_handler["output"],
            "errors":output_handler["errors"]
        }


        return Response(code_output)
    
class ExecutionHandler:
    def handle_execution(self,language,user_codefile,testcaseJson,name):
        driver_code_instance=DriverCodeMiddleware.DrivercodeLanguage(language)
        Combined_code=driver_code_instance.DriverCodeGenerator(user_codefile,testcaseJson)
       
        ExecutioncodeInstance=ExecuteCodeFactory.CodeExecution(language)
        code_output=ExecutioncodeInstance.Execute(Combined_code,name)
        return code_output

