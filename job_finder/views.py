from django.shortcuts import render
from .models import Job, Resume

def baseView(request):
    return render(request, 'job_finder/base_view.html', {'jobs': Job})