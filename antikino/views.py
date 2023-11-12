from django.shortcuts import render

def Home(reuest):
    return render(reuest, 'main.html')
