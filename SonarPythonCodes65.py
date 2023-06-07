import subprocess
input = request.get('input')
subprocess.run(["/usr/bin/find", input]) # Sensitive