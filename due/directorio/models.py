from django.db import models
#from django.utils.timezone import now
#from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    cuit = models.CharField(max_length=15, verbose_name="CUIT")
    company_name = models.CharField(max_length=100, verbose_name="Razón Social")
    activity_code = models.CharField(max_length=6, verbose_name="CLANAE")
    city = models.CharField(max_length=50, verbose_name="Departamento")
    contact = models.CharField(max_length=100, verbose_name="Datos de contacto")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de última modificación", auto_now=True)

    class Meta:
        verbose_name = "empresa"
        verbose_name_plural = "empresas"
        ordering = ["company_name"]
    
    def __str__(self) -> str:
        return self.company_name
"""
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de última modificación", auto_now=True)

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ["created"]
    
    def __str__(self) -> str:
        return self.title
"""    
