from django.shortcuts import render, HttpResponse, redirect
from .models import StudentData
from django.contrib import messages
from django.db import connection

# Home View
def home(request):
    data = StudentData.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context)

# About Page
def about(request):
    return render(request, 'about.html')

# Insert Data
def insert(request):
    if request.method == 'POST':
        name = request.POST.get('student')
        email = request.POST.get('email')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        language = request.POST.get('language')

        query = StudentData(studentName=name, email=email, branch=branch,
                            year=year, language=language)
        query.save()
        messages.success(request, "Data Inserted Successfully")
        return redirect('/')
    
    return redirect('/')

# Delete Data & Reset ID
def deleteData(request, id):
    try:
        dt = StudentData.objects.get(id=id)
        dt.delete()
        messages.error(request, "Data Deleted Successfully")

        # Reset Auto-Increment Sequence (Only for SQLite & PostgreSQL)
        with connection.cursor() as cursor:
            cursor.execute("DELETE FROM sqlite_sequence WHERE name='appname_studentdata';")  # Change 'appname' to your Django app name
        
    except StudentData.DoesNotExist:
        messages.error(request, "Data Not Found")

    return redirect('/')

# Update Data
def updateData(request, id):
    try:
        edit = StudentData.objects.get(id=id)

        if request.method == 'POST':
            name = request.POST.get('student')
            email = request.POST.get('email')
            branch = request.POST.get('branch')
            year = request.POST.get('year')
            language = request.POST.get('language')

            edit.studentName = name
            edit.email = email
            edit.branch = branch
            edit.year = year
            edit.language = language
            edit.save()

            messages.warning(request, "Data Updated Successfully")
            return redirect('/',reset_id=id)

        context = {"dt": edit}
        return render(request, 'update.html', context)

    except StudentData.DoesNotExist:
        messages.error(request, "Data Not Found")
        return redirect('/')
