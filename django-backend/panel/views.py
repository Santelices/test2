from django.shortcuts import render 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , CreateView 
from .models import Alumno , Profesor
from .form import AlumnoForm
from .form import ProfesorForm

from django.views.generic.edit import UpdateView


from django.db.models import Q
# Create your views here.

class ProfesorListView(LoginRequiredMixin, ListView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'panel/profesores.html'
    context_object_name = 'profesores'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        return Profesor.objects.filter(
            Q(deleted=False),
            Q(id_profesor__icontains=search) |
            Q(nombre_profesor__icontains=search)
        )

class AlumnoListView(LoginRequiredMixin, ListView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'panel/alumnos.html'
    context_object_name = 'alumnos'
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

    def get_queryset(self, **kwargs):
        search = self.request.GET.get('search', '')
        return Alumno.objects.filter(
            Q(deleted=False),
            Q(id_alumno__icontains=search) |
            Q(Nombres__icontains=search)
        )

class AlumnoCreateView(LoginRequiredMixin, CreateView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'panel/form-alumno.html'
    form_class = AlumnoForm


    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        
        return '/panel/alumnos'
    



class ProfesorCreateView(LoginRequiredMixin, CreateView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'panel/form-profesor.html'
    form_class = ProfesorForm


    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        
        return '/panel/profesores'
    


