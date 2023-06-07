import os

@app.route("/kill-pid/<pid>")
def send_signal(pid):
    os.kill(pid, 9)  # Sensitive

@app.route("/kill-pgid/<pgid>")
def send_signal(pgid):
    os.killpg(pgid, 9)  # Sensitive