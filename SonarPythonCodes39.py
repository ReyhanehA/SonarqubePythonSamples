from django.shortcuts import render

def check_cookie(request):
    response = render(request, "welcome.html")

    if not "sessionid" in request.COOKIE:
        cookie = request.GET.get("cookie")
        response.set_cookie("sessionid", cookie)  # Noncompliant

    return response