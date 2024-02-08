from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.home, name='home'),
    path('projects/', views.projects),
    path('projects/<int:id>/', views.buscar_proyecto)
]
