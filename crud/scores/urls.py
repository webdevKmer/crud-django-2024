from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_scores, name='scores'),
    path('add/', views.add_score, name='add'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/', views.score_detail, name='score_detail'),
    path('edit/<int:pk>/', views.edit_score, name='edit'),
]
