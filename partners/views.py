from django.shortcuts import render

from .models import Partner


def partners(request):
    partners = Partner.objects.all()
    return render(request, 'partners/partners.html', {'partners': partners})
