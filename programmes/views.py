from django.shortcuts import render

from .models import Programme


def programmes(request):
    programmes = Programme.objects.all()
    return render(request, 'programmes/programmes.html', {'programmes': programmes})
