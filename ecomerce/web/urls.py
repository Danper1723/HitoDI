from django.urls import path
from web import views

urlpatterns = [
	path("", views.tienda_index, name="tienda_index"),
    path("<int:pk>/", views.tienda_detalle, name="tienda_detalle"),
]