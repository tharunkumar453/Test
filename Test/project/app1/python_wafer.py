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