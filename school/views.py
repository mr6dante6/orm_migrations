from django.shortcuts import render
from .models import Student


def students_list(request):
    students = Student.objects.prefetch_related('teachers').all()
    for student in students:
        print(f"Student: {student.name}")
        for teacher in student.teachers.all():
            print(f"Teacher: {teacher.name} ({teacher.subject})")
    context = {'students': students}
    return render(request, 'school/students_list.html', context)
