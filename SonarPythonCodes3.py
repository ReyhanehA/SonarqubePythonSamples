from flask import Flask, redirect

app = Flask("example")

@app.route("/redirect")
def redirect():
    url = request.args["url"]
    return redirect(url) # Noncompliant
