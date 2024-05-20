from django.shortcuts import render, get_object_or_404
from .models import Job, Resume

def job_list(request):
    jobs = Job.objects.all
    return render(request, 'job_finder/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    jobs = get_object_or_404(Job, pk=pk)
    return render(request, 'job_finder/job_detail.html', {'jobs': jobs})