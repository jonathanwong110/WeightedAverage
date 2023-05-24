from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Assignment
from .forms import AssignmentForm


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
