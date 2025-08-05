import os
import sys
from mangum import Mangum
from django.core.asgi import get_asgi_application

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OnlineTestingSystem.settings")

import django
django.setup()

application = get_asgi_application()
handler = Mangum(application)
