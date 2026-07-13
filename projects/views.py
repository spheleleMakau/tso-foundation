from django.shortcuts import render

from .models import Project


def projects(request):
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {'projects': projects})


def project_detail(request, slug):
    project = Project.objects.filter(slug=slug).first()
    return render(request, 'projects/project_detail.html', {'slug': slug, 'project': project})
