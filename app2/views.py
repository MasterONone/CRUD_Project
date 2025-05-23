from django.shortcuts import render, get_object_or_404, redirect
from .models import Student
from .forms import StudentForm


def student_list(request):
    students = Student.objects.all()
    return render(request, 'app2/student_list.html', {'students': students})


def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'app2/student_form.html', {'form': form})


def student_update(request, StudentID):
    student = get_object_or_404(Student, StudentID=StudentID)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'app2/student_form.html', {'form': form})


def student_delete(request, StudentID):
    student = get_object_or_404(Student, StudentID=StudentID)
    if request.method == "POST":
        student.delete()
        return redirect('student_list')
    return render(request, 'app2/student_confirm_delete.html', {'student': student})
