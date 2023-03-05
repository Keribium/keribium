from django.shortcuts import render


# Create your views here.
def login_index(request):
    return render(request, "login/index.html")

def error_404(request):
    return render(request, "404.html")

def error_500(request):
    return render(request, "500.html")