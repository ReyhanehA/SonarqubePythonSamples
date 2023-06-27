#Python 3

subprocess.run(cmd, shell=True)  # Sensitive
subprocess.Popen(cmd, shell=True)  # Sensitive
subprocess.call(cmd, shell=True)  # Sensitive
subprocess.check_call(cmd, shell=True)  # Sensitive
subprocess.check_output(cmd, shell=True)  # Sensitive
os.system(cmd)  # Sensitive: a shell is always spawn

