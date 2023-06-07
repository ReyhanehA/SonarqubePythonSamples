def ping():
    cmd = "ping -c 1 %s" % request.args.get("host", "www.google.com")
    status = os.system(cmd) # Noncompliant
    return str(status == 0)