from django.shortcuts import render

# Create your views here.

def students(request):
    context = {}
    return render(request, 'students/index.html', context)
