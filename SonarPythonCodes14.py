from flask import render_template

@app.route('/hello/<name>')
def hello(name=None):
    hello = f"<h1>Hello { name }</h1>"
    return render_template('hello.html', hello=hello)
