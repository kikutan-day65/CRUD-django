from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('create_data/', views.create_data, name='create-data'),
    path('update_data/<str:pk>/', views.update_data, name='update-data'),
    path('delete_data/<str:pk>/', views.delete_data, name='delete-data'),
]