from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('create_data/', views.create_data, name='create-data'),
]