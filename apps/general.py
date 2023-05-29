from django.shortcuts import render, redirect

def Home(request):
    return render(request, 'home.html')