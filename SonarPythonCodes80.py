For Django:

# No method restriction
def view(request):  # Sensitive
    return HttpResponse("...")
-------------------------------------------------
@require_http_methods(["GET", "POST"])  # Sensitive
def view(request):
    return HttpResponse("...")
-------------------------------------------------
For Flask:

@methods.route('/sensitive', methods=['GET', 'POST'])  # Sensitive
def view():
    return Response("...", 200)
