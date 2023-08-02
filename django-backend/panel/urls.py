from django.urls import path
from .views import *

urlpatterns = [
    path('alumnos', AlumnoListView.as_view(), name='alumnos'),
    path('panel/form-alumno/', AlumnoCreateView.as_view(), name='form-alumno'),
    path('panel/form-alumno/<str:pk>/', AlumnoUpdateView.as_view(), name='form-alumno-editar'),
    path('panel/confirm_delete/<str:pk>/', AlumnoDeleteView.as_view(), name='form-alumno-eliminar'),



    path('profesores', ProfesorListView.as_view(), name='profesores'),
    path('panel/form-profesor/', ProfesorCreateView.as_view(), name='form-profesor'),
    path('panel/form-profesor/<str:pk>/', ProfesorUpdateView.as_view(), name='form-profesor-editar'),
    path('panel/confirm_delete/<str:pk>/', ProfesorDeleteView.as_view(), name='form-profesor-eliminar'),

]
