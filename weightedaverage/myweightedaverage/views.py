from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Assignment


# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Assignment
    template_name = 'home.html'


class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignment_details.html'
