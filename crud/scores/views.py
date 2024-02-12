from django.shortcuts import render, redirect
from .models import Score
from .forms import AddForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def delete(request, pk):
    Score.objects.get(id=pk).delete()
    return redirect('scores:all')

def edit(request, pk):
    item = Score.objects.get(id=pk)
    form = AddForm(instance=item)
    if request.method == 'POST':
        form = AddForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('scores:all')
    context = {
        'form' : form,
        'score' : item
    }
    return render(request, 'scores/edit.html', context)

def add(request):
    form = AddForm()
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('scores:all')
    context = {
        'form' : form
    }
    return render(request, 'scores/add.html', context)

def detail(request, pk):
    score = Score.objects.get(id=pk)
    context = {
        'score' : score
    }
    return render(request, 'scores/detail.html', context)

def all_scores(request):
    scores = Score.objects.all()
    context = {
        'scores' : scores,
    }
    return render(request, 'scores/all_scores.html', context)