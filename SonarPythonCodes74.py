For os.umask:

os.umask(0)  # Sensitive
-----------------------------------------
For os.chmod, os.lchmod, and os.fchmod:

os.chmod("/tmp/fs", stat.S_IRWXO)   # Sensitive
os.lchmod("/tmp/fs", stat.S_IRWXO)  # Sensitive
os.fchmod(fd, stat.S_IRWXO)         # Sensitive
