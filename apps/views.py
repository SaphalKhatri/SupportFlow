from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.middleware.csrf import get_token
# Create your views here.
@require_GET
def health_check(request):
    csrf_token=get_token(request)
    return JsonResponse({
        "status":"healthy",
        "service":"Supportflow API",
        "csrf_token":csrf_token,
    })
