import os, sys, traceback
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tso_foundation.settings')
import django
from django.template import TemplateSyntaxError

django.setup()
from django.template.loader import get_template

templates = ['home/index.html', 'base.html', 'includes/header.html', 'includes/footer.html']
for tpl in templates:
    try:
        t = get_template(tpl)
        print('Loaded', tpl)
    except TemplateSyntaxError as e:
        print('TemplateSyntaxError in', tpl, e)
        traceback.print_exc()
    except Exception as e:
        print('Error loading', tpl, e)
        traceback.print_exc()
