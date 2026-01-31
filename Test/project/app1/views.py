from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView
import subprocess
import tempfile
import os
from .models import testcase_table
from .serializers import test_case_serializer
import json
class submit(APIView):
    """
    A view that can accept POST requests with JSON content.
    """
    parser_classes = [MultiPartParser]

    def post(self, request):
        text=request.data.get("name")
        file=request.FILES["file"].read().decode("utf-8")
        problem_id=request.data.get("problem_id")
        
        print(problem_id)
        test_case_file=testcase_table.objects.get(problem_id=problem_id)
        # serializer =test_case_serializer(test_case_file)
        # serializer =serializer.data['test_cases']
        # print(serializer)
        with test_case_file.test_cases.open("r") as j:

            tc=json.load(j)
           
        print(tc)
        print(111)
       

        code_file=combined_file_cpp(file,tc)  # pyright: ignore[reportUnknownArgumentType]
        print(code_file)
        with tempfile.NamedTemporaryFile(mode="w+",suffix=".cpp",delete=False)as t:
            t.write(code_file)
            t.flush()
            

            path=os.path.join(t.name)
            t.close()
        
        try:
            x=subprocess.run(["g++ ",path,"-o","tharun.exe"],capture_output=True,text=True,universal_newlines=True)
            v=subprocess.run(["tharun.exe"],capture_output=True,text=True,universal_newlines=True)
        finally:
            pass

        return Response({"message":"data recived ","filename":request.FILES["file"].name,"output":x.stdout.strip(),"error":x.stderr.strip()})
def combined_file_python(file,test_casess):
    return f'''# user code##
{file}
##user code ends###
#test cases start###
def _test_user_code():
    a=sol()
    inputs=[tc["input"] for tc in {test_casess['cases']}]
    ans=[tc["expected"] for tc in {test_casess['cases']}]

    for i in range (len(inputs)):
        
        method=a.max_element(inputs[i])
        if(method!=ans[i]):
           print(f"wrong answer at test case")
           return
    print("code exicuted sucessfully")
_test_user_code()
### test cases ends ##'''


def combined_file_cpp(file,test_casess):
    return f'''# user code##
{file}
int main(){{
    solution a=solution();
    vector<vector<int>>inputs={{tc["input"] for auto tc in {test_casess['cases']}}};
    vectot<int>ans={{tc["expected"] for auto tc in {test_casess['cases']}}};

    for(int i=0;i<inputs.size();i++){{
        
        int method=a.print_element(inputs[i]);
        if(method!=ans[i]){{
           cout<<"wrong answer at test case";
           return 0;
        }}
    cout<<"code exicuted sucessfully";
}}
'''