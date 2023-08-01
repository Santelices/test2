from django.urls import path
from .views import AlumnoListView, ProfesorListView, AlumnoCreateView, ProfesorCreateView


urlpatterns = [
    path('alumnos', AlumnoListView.as_view(), name='alumnos'),
    path('profesores', ProfesorListView.as_view(), name='profesores'),
    path('panel/form-alumno/', AlumnoCreateView.as_view(), name='form-alumno'),
    path('panel/form-profesor/', ProfesorCreateView.as_view(), name='form-profesor'),
]


