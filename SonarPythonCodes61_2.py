#    the CSRF protection is disabled on a view:

@csrf_exempt # Sensitive
def example(request):
    return HttpResponse("default")