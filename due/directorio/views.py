from django.shortcuts import render, redirect
from .models import Company
from .forms import AgregarForm
from django.urls import reverse

# Create your views here.
def listado(request):
   companies = Company.objects.all()
   return render(request, "directorio/listado.html", {'companies': companies})

def agregar(request):
   agregar_form = AgregarForm()
   
   if request.method == "POST":
      agregar_form = AgregarForm(data=request.POST)
      if agregar_form.is_valid():
         cuit = request.POST.get('cuit','')
         company_name = request.POST.get('company_name','')
         activity_code = request.POST.get('activity_code','')
         city = request.POST.get('city','')
         contact = request.POST.get('contact','')
         
         return redirect(reverse('listado')+"?ok")
   return render(request, "directorio/agregar.html", {'form':agregar_form})