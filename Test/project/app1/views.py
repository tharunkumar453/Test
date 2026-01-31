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
           

       

        code_file=combined_file_cpp(file,tc)  # pyright: ignore[reportUnknownArgumentType]
        print(code_file)
        with tempfile.NamedTemporaryFile(mode="w+",suffix=".cpp",delete=False)as t:
            t.write(code_file)
            t.flush()
            
            path1=os.curdir+"/tharun.exe"        
            # path=os.path.join(t.name)

            t.close()
        print(path1)
        try:
            y=subprocess.run(["g++",t.name,"-o","tharun.exe"],capture_output=True,text=True,universal_newlines=True)
            x=subprocess.run([path1],capture_output=True,text=True,universal_newlines=True)
           
        
        finally:
            os.remove(t.name)
            os.remove(path1)


        return Response({"message":"data recived ","filename":request.FILES["file"].name,"output":x.stdout.strip(),"error":x.stderr.strip()})
def combined_file_python(file,test_casess):
    inputs=[tc["input"] for tc in test_casess['cases']]
    ans=[tc["expected"] for tc in test_casess['cases']]
    method=test_casess["method"]
    return f'''
{file}

def _test_user_code():
    a=sol()
    for i,test in enumerate({inputs}):
       
        returns=a.{method}(test)
        if(returns!={ans}[i]):
           print(f"wrong answer at test case")
           return
    print("code exicuted sucessfully")
_test_user_code()
'''


def combined_file_cpp(file,test_casess):
    tests = ""
   
    for i, tc in enumerate(test_casess["cases"]):
        tests += f"""
        {{
            vector<int> input = {python_list_to_cpp_vector(tc["input"])};
            int expected = {tc["expected"]};
            {test_casess["retrun_type"]} output = a.{test_casess["method"]}(input);
            if (output != expected) {{
                cout << "Wrong Answer at test case {i+1}" << endl;
                return 0;
            }}
        }}
        """

    return f'''
{file}
int main(){{
    Solution a=Solution();
    {tests}
    cout<<"code exicuted sucessfully";
    return 0;
   
    }}
'''
def  python_list_to_cpp_vector(py_list):
    cpp_vector = "{"
    cpp_vector += ", ".join(str(x) for x in py_list)
    cpp_vector += "}"
    return cpp_vector