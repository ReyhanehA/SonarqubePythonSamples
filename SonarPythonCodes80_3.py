#For Django:
@require_http_methods(["GET", "POST"])  # Sensitive
def view(request):
    return HttpResponse("...")