import subprocess
import tempfile
import os

class code_execution:
    def execute_code(self,file,test_casess):
        pass

#Execute python code with test cases
class code_execution_python(code_execution):
    def execute_code(self,code_file,file_name):
    
       
     
        subprocess_anycode_instance=subprocess_anycode()
        return subprocess_anycode_instance.execute_any_code(code_file,"python",file_name)

#Execute C++ code with test cases
class code_execution_cpp(code_execution):
    def execute_code(self,code_file,file_name):
     
       
        subprocess_anycode_instance=subprocess_anycode()
        return subprocess_anycode_instance.execute_any_code(code_file,"cpp",file_name)
        


# process any code using subprocess   
class subprocess_anycode:
    def execute_any_code(self,code_file,language,file_names):
        with tempfile.TemporaryDirectory()as temp_dir:
            if(language=="python"):
                file_name="code.py"
            elif(language=="cpp"):
                file_name="code.cpp"
            path_dir=os.path.join(temp_dir,file_name)

            with open(path_dir,'w+') as code_file_handle:
                code_file_handle.write(code_file)
                code_file_handle.flush()
            code_file_handle.close()
           
            if(language=="python"):
                command=["python",path_dir]
            elif(language=="cpp"):
                command=["./a.out"]
                
                compile_process=subprocess.run(["g++",path_dir,"-o","a.out"],capture_output=True,text=True,universal_newlines=True)
                if(compile_process.returncode!=0):
                    return{"message":"Compilation Error","filename":file_name,"output":"","errors":compile_process.stderr.strip()}
                    
            
            process_output=subprocess.run(command,capture_output=True,text=True,universal_newlines=True)
        return{"message":" your code received!!","filename":file_names,"output":process_output.stdout.strip(),"errors":process_output.stderr.strip()}