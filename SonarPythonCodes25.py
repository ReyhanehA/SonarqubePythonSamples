client = SSHClient()
client.connect("example.org", username=USER, password=PASS)
client.exec_command(request.args.get("cmd")) # Noncompliant