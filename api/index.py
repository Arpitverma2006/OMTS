import os
import sys
from fastapi import FastAPI
from mangum import Mangum

# Add Django project to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "omts.settings")

import django
from django.core.asgi import get_asgi_application

django.setup()

# Wrap Django ASGI inside FastAPI
django_app = get_asgi_application()
app = FastAPI()

@app.middleware("http")
async def django_adapter(request, call_next):
    # Let Django ASGI handle it
    return await django_app(request.scope, request.receive, request.send)

handler = Mangum(app)  # Required by Vercel
