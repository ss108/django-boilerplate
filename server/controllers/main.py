from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import ensure_csrf_cookie 
from django.http import HttpResponse

from django_quicky import routing

url, urlpatterns = routing()

@url("^$")
# @ensure_csrf_cookie
def index(req):
    return HttpResponse("hehehn")
