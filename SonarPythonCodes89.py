Python 3

subprocess.run(cmd, shell=True)  # Sensitive
subprocess.Popen(cmd, shell=True)  # Sensitive
subprocess.call(cmd, shell=True)  # Sensitive
subprocess.check_call(cmd, shell=True)  # Sensitive
subprocess.check_output(cmd, shell=True)  # Sensitive
os.system(cmd)  # Sensitive: a shell is always spawn
----------------------------------------------------
Python 2

cmd = "when a string is passed through these function, a shell is spawn"
(_, child_stdout, _) = os.popen2(cmd)  # Sensitive
(_, child_stdout, _) = os.popen3(cmd)  # Sensitive
(_, child_stdout) = os.popen4(cmd)  # Sensitive


(child_stdout, _) = popen2.popen2(cmd)  # Sensitive
(child_stdout, _, _) = popen2.popen3(cmd)  # Sensitive
(child_stdout, _) = popen2.popen4(cmd)  # Sensitive
