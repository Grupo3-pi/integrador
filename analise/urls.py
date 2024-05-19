from django.urls import path
from . import views

urlpatterns = [
    path('', views.flexmonster_view, name='flexmonster_view'),
    path('flexmonster_data/', views.flexmonster_data, name='flexmonster_data'),
]