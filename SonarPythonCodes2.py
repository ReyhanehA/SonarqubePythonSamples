@app.route('/login')
def login():
    dynamodb = AWS_SESSION.client('dynamodb')

    username = request.args["username"]
    password = request.args["password"]

    dynamodb.scan(
        FilterExpression= "username = " + username + " and password = " + password, # Noncompliant
        TableName="users",
        ProjectionExpression="username"
    )
