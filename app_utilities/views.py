from django.shortcuts import render

def get_home(request):
    return render(request, 'Home.html')