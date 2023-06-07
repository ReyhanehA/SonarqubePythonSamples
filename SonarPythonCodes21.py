from xml.etree import ElementTree
from flask import request

@app.route('/authenticate')
def authenticate():
    username = request.args['username']
    password = request.args['password']
    expression = "./users/user[@name='" + username + "'][@pass='" + password + "']"
    tree = ElementTree.parse('resources/users.xml')

    if tree.find(expression) is None:
        return "Invalid credentials", 401
    else:
        return "Success", 200