"""
URL configuration for tso_foundation project.
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('about/', include('about.urls', namespace='about')),
    path('programmes/', include('programmes.urls', namespace='programmes')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('gallery/', include('gallery.urls', namespace='gallery')),
    path('partners/', include('partners.urls', namespace='partners')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots_txt'),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml'), name='sitemap'),
]
