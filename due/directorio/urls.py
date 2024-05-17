from django.urls import path
from . import views

urlpatterns = [
   path('', views.listado, name="listado"),
#   path('category/<int:category_id>/', views.category, name="category")
]