import json
class TotalCOdeCombiner:
    def combine_originl_tests(self,file,tests):
        x=f'''
{file}  
{tests}
'''     
        print(x)
        return x   
class PythonCombiner:
    @staticmethod
    def combined_file_python(file,test_casess):
        inputs=[tc["input"] for tc in test_casess['cases']]
        ans=[tc["expected"] for tc in test_casess['cases']]
        method=test_casess["method_name"]
        x=f'''
def parse(x):
    if isinstance(x,list):
        return[parse(v) for v in x]
    if isinstance(x,dict):
        return {{ k: parse(v) for k,v in x.items()}}
    return x
def driver_code():
    a=Solution()
    func=getattr(a,'{method}')
    for  i,(x,y) in enumerate(zip{inputs,ans}):
        args=parse(x)
        out=func(*args)
        exp=parse(y)
        print(out)
        print(exp)
        if(out!=exp):
            print("error at test case",i+1)
            return
    print("Accepted")
driver_code()
'''   
        return TotalCOdeCombiner().combine_originl_tests(file,x)
        

class CppCombiner:
    @staticmethod
    def combined_file_cpp(file,test_casess):
        print(test_casess)
        dump_json=json.dumps(test_casess,indent=2)        
        x=f'''

#include <bits/stdc++.h>
#include "/workspaces/Test/Test/project/app1/include/json.hpp"

using json = nlohmann::json;
using namespace std;


void driver_code() {{
    Solution a;

    json data = R"({dump_json})"_json;

    auto cases = data["cases"];

    for (int i = 0; i < cases.size(); i++) {{
        for(int j=0;j<{test_casess["signature"]}.size();j++){{
            auto arg_i=cases[i]["input"][0].get<{test_casess["signature"]}>();
            
        }}
       
        auto expected = cases[i]["expected"].get<{test_casess["return_type"]}>();

        auto output = a.ReverseString(args);

        if (output != expected) {{
            cout << "Error at test case " << i + 1 << endl;
            return;
        }}
    }}

    cout << "Acceted" << endl;
}}

int main() {{
    driver_code();
    return 0;
}}


'''
        return TotalCOdeCombiner().combine_originl_tests(file,x)