file = open("/tmp/temporary_file","w+") # Sensitive

tmp_dir = os.environ.get('TMPDIR') # Sensitive
file = open(tmp_dir+"/temporary_file","w+")
