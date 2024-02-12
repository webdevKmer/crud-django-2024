from django.shortcuts import render, redirect
from .models import Student
from scores.models import Score
from .forms import AddStudentForm
# Create your views here.

def students(request):
    students = Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'students/all_students.html', context)

def add(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:all')
    else :
        form = AddStudentForm()

    context = {
        'form' : form,
    }
    return render(request, 'students/add.html', context)

def edit(request, pk):
    student = Student.objects.get(id=pk)
    if request.method == 'POST':
        form = AddStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('students:all')
    else :
        form = AddStudentForm(instance=student)

    context = {
        'form' : form,
        'student': student
    }
    return render(request, 'students/edit.html', context)

def delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return redirect('students:all')

def detail(request, pk):
    student = Student.objects.get(id=pk)
    scores = Student.scores
    context = {
        'student': student,
        'scores' : scores
    }
    return render(request, 'students/detail.html', context)

