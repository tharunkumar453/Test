import tempfile
import os
import subprocess
with tempfile.TemporaryDirectory() as f:
	path=os.path.join(f,"tarun.py")
	with open(path,"w")as o:
		o.write("print(1)")
		x=subprocess.run(["python",path],capture_output=True,text=True)
print(x.stdout)