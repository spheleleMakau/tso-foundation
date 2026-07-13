from django.shortcuts import render

from .models import HeroSlide


def index(request):
    slides = HeroSlide.objects.filter(is_active=True)[:4]
    return render(request, 'home/index.html', {'hero_slides': slides})
