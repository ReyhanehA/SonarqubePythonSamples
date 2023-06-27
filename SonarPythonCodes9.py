from django.shortcuts import render

def hello(request):
        name = request.GET.get("name")
        hello = f"<h1>Hello { name }</h1>"
        return render(request, 'hello.html', {'hello': hello})