from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *
from .models import Alumno , Profesor
from .form import AlumnoForm
from .form import ProfesorForm



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
    paginate_by = 100


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

class AlumnoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'panel/form-alumno.html'
    form_class = AlumnoForm
    model = Alumno

    def get_success_url(self):
         return '/panel/alumnos'  # Redirigir a la lista de alumnos después de editar uno

    def get_object(self, queryset=None):
        # Obtener el objeto Alumno que queremos editar
        pk = self.kwargs.get('pk')
        return get_object_or_404(Alumno, pk=pk)

class ProfesorUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'panel/form-profesor.html'
    form_class = ProfesorForm
    model = Profesor

    def get_success_url(self):
         return '/panel/profesores'  # Redirigir a la lista de alumnos después de editar uno

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profesor, pk=pk)

class ProfesorDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    model = Profesor
    template_name = 'panel/confirm_delete.html'
    success_url = reverse_lazy('profesores')  # Redirigir a la lista de alumnos después de eliminar uno

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Profesor, pk=pk)

class AlumnoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/seguridad/login/'
    redirect_field_name = 'redirect_to'
    model = Alumno
    template_name = 'panel/confirm_delete.html'
    success_url = reverse_lazy('Alumnos')  # Redirigir a la lista de alumnos después de eliminar uno

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Alumno, pk=pk)
