from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.students, name='all'),    
    path('add/', views.add, name='add'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/', views.detail, name='detail'),
    path('edit/<int:pk>/', views.edit, name='edit'),
]
