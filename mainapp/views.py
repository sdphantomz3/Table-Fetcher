from django.shortcuts import render
from .models import *

# Create your views here.
def display_table_data(request):
    # Retrieve all scraped data from the database
    table_data = TableData.objects.all()
    return render(request, 'table_data.html', {'table_data': table_data})