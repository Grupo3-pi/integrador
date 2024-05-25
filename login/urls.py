from django.urls import path
from django.contrib.auth import views as auth_views
from .views import analise_view

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('analise/', analise_view, name='analise'),
]