from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import problem_table,UserBoard
from .serializers import UserDashboardSerializer    


from app1.MiddleWare import DriverCodeMiddleware,ExecuteCodeFactory
from app1.workers import WriteInFile

class submit(APIView):
  
    parser_classes = [MultiPartParser]

    def post(self, request):
        user_email=request.data.get("email")
        name=request.data.get("name")
        user_codefile=request.FILES["file"].read().decode("utf-8")
        problem_id=request.data.get("problem_id")
        language=request.data.get("language")
        test_case_file=problem_table.objects.get(problem_id=problem_id)
        has_previously_correct=UserBoard.objects.filter(email=user_email,problem=test_case_file,has_done=True)
        if has_previously_correct.exists():
            return Response("you alredy submitt this oone correctluy this submission not ")


     
        print(type(test_case_file))

        testcaseJson=WriteInFile.write_in_file(test_case_file)
        code_output=ExecutionHandler().handle_execution(language,user_codefile,testcaseJson,name)

        if code_output["output"]=="Accepted":
            UserBoard.objects.create(email=user_email,problem=test_case_file,has_done=True,language_used=language)

        else:
            UserBoard.objects.create(email=user_email,problem=test_case_file,language_used=language)



        return Response(code_output)
    
class ExecutionHandler:
    def handle_execution(self,language,user_codefile,testcaseJson,name):
        driver_code_instance=DriverCodeMiddleware.DrivercodeLanguage(language)
        Combined_code=driver_code_instance.DriverCodeGenerator(user_codefile,testcaseJson)
       
        ExecutioncodeInstance=ExecuteCodeFactory.CodeExecution(language)
        code_output=ExecutioncodeInstance.Execute(Combined_code,name)
        return code_output



# User Dashboard APIs
class UserDashboardView(APIView):
    parser_classes = [MultiPartParser]
    def get(self, request):
        user_email = request.data.get("email")
        if not user_email:
            return Response({"detail": "please Register"}, status=status.HTTP_400_BAD_REQUEST)

        user = UserBoard.objects.filter(email=user_email,has_done=True)
        serializer = UserDashboardSerializer(user,many=True)
        data=serializer.data
        return Response(data, status=status.HTTP_200_OK)
 

class TotalSubmissions(APIView):
    def get(self,request):
        user_email=request.data.get("email")
        if not user_email:
            return Response({"detail": "please Register"}, status=status.HTTP_400_BAD_REQUEST)
        count=UserBoard.objects.filter(email=user_email).count()
        return Response(count,status=status.HTTP_200_OK)

        
        


       
        







        
