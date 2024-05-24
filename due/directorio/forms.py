from django import forms

class AgregarForm(forms.Form):
    cuit = forms.CharField(label="CUIT", required=True)
    company_name = forms.CharField(label="Razón Social", required=True)
    activity_code = forms.CharField(label="CLANAE", required=True)
    city = forms.CharField(label="Departamento", required=True)
    contact = forms.CharField(label="Datos de contacto")