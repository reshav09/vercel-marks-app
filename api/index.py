from vercel_python_wsgi import make_wsgi_app
from asgi import app as asgi_app
from mangum import Mangum
import uvicorn

# Adapt FastAPI (ASGI) to WSGI for Vercel
app = make_wsgi_app(asgi_app)

