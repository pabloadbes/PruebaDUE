from django.shortcuts import render
from .models import Company

# Create your views here.
def listado(request):
   companies = Company.objects.all()
   return render(request, "directorio/listado.html", {'companies': companies})