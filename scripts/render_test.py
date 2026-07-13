import os, sys, traceback
# Ensure project root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tso_foundation.settings')
import django
from django.template import TemplateSyntaxError
try:
    django.setup()
    from django.template.loader import get_template
    t = get_template('home/index.html')
    print('Template loaded OK')
    print(t.render({}))
except TemplateSyntaxError as e:
    print('TemplateSyntaxError:', e)
    traceback.print_exc()
except Exception as e:
    print('Error:', e)
    traceback.print_exc()
