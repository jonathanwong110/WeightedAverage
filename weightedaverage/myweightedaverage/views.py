from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Assignment
from .forms import AssignmentForm
from django.urls import reverse_lazy


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Assignment
    template_name = 'home.html'


class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignment_details.html'


class AddAssignmentView(CreateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'add_assignment.html'
    # fields = '__all__'


class UpdateAssignmentView(UpdateView):
    model = Assignment
    form_class = AssignmentForm
    template_name = 'update_assignment.html'
    # fields = '__all__'


class DeleteAssignmentView(DeleteView):
    model = Assignment
    template_name = 'delete_assignment.html'
    success_url = reverse_lazy('home')
