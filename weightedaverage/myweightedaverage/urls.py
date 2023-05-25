from django.urls import path
# from . import views
from .views import HomeView, AssignmentDetailView, AddAssignmentView, UpdateAssignmentView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('assignment/<int:pk>', AssignmentDetailView.as_view(), name='assignment-detail'),
    path('add_assignment/', AddAssignmentView.as_view(), name='add_assignment'),
    path('assignment/edit/<int:pk>', UpdateAssignmentView.as_view(), name='update_assignment'),
]
