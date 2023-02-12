from django.shortcuts import render


# Create your views here.
def login_index(request):
    return render(request, "login/index.html")
