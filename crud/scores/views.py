from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def all_scores(request):
    return render(request, 'scores/all_scores.html')