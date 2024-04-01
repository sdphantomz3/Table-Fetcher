from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_table_data, name='display_table_data'),
]
