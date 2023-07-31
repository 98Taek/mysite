from django.urls import path, include
from account import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
]
