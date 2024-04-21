import sys
import os
import subprocess
cmd=["python3","engine2.py"]
q="abc"
cmd.append(q)
p=subprocess.run(cmd,capture_output=True,text=True)
a=p.stdout.strip()
print("Answer:", a)
