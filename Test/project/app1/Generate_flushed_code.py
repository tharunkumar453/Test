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
        tests = ""
        if test_casess["parameters"] == "list_of_integers":
            for i, tc in enumerate(test_casess["cases"]):
                tests += f'''
    std::vector<int> test{i+1} = {{{', '.join(map(str, tc["input"]))}}};
    int expected{i+1} = {tc["expected"]};
    int output{i+1} = Solution().{test_casess["method_name"]}(test{i+1});
    if (output{i+1} != expected{i+1}) {{
        std::cout << "wrong answer at test case {i+1}" << std::endl;
        return 0;
    }}
'''
        elif test_casess["parameters"] == "integer":
            for i, tc in enumerate(test_casess["cases"]):
                tests += f'''
    int test{i+1} = {tc["input"]};
    int expected{i+1} = {tc["expected"]};
    int output{i+1} = Solution().{test_casess["method_name"]}(test{i+1});
    if (output{i+1} != expected{i+1}) {{
        std::cout << "wrong answer at test case {i+1}" << std::endl;
        return 0;
    }}
'''
        elif test_casess["parameters"] == "string":
            for i, tc in enumerate(test_casess["cases"]):
                tests += f'''
    std::string test{i+1} = "{tc["input"]}";
    std::string expected{i+1} = "{tc["expected"]}";
    std::string output{i+1} = Solution().{test_casess["method_name"]}(test{i+1});
    if (output{i+1} != expected{i+1}) {{
        std::cout << "wrong answer at test case {i+1}" << std::endl;
        return 0;
    }}
'''
        else:
            raise ValueError("Unsupported parameter type")
        x=f'''
int main() {{
{tests}
    std::cout << "453@" << std::endl;
    return 0;
}}'''

        return TotalCOdeCombiner().combine_originl_tests(file,x)

