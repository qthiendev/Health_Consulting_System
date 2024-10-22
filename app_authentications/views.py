from django.shortcuts import render

def get_login(request):
    return render(request, 'Login.html')