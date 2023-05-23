from django.urls import path
# from . import views
from .views import HomeView, AssignmentDetailView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('assignment/<int:pk>', AssignmentDetailView.as_view(), name='assignment-detail'),
]
