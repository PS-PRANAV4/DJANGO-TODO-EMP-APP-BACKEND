from django.urls import path
from . import views

urlpatterns = [
    path('department/', views.departmentapi),
    path('department/<int:id>/', views.departmentapi),
    path('emp/', views.employe),
    path('emp/<int:id>/', views.employe),
]