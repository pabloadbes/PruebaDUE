from django.urls import path
from . import views

urlpatterns = [
   path('listado/', views.listado, name="listado"),
   path('agregar/', views.agregar, name="agregar"),
#   path('category/<int:category_id>/', views.category, name="category")
]