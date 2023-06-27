#For Flask:

@methods.route('/sensitive', methods=['GET', 'POST'])  # Sensitive
def view():
    return Response("...", 200)