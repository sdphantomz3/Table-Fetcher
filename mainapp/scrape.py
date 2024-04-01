# scrape.py
import requests
from bs4 import BeautifulSoup
from .models import TableData

def scrape_website_and_save_data():
    # Delete all existing TableData objects
    TableData.objects.all().delete()

    url = 'https://jbms.pk/solar-panel-price-in-pakistan/'  # URL of the webpage
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all tables on the webpage
    tables = soup.find_all('table')

    # Loop through each table and extract data
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            columns = row.find_all(['th', 'td'])
            if columns:
                # Extract data from each column, handling different column lengths
                column_data = [col.text.strip() for col in columns]
                if len(column_data) >= 2:
                    # Check if there are at least two columns
                    if len(column_data) == 3:
                        # If there are three columns, use all of them
                        column1 = column_data[0]
                        column2 = column_data[1]
                        column3 = column_data[2]
                    elif len(column_data) == 2:
                        # If there are only two columns, set the third column to an empty string
                        column1 = column_data[0]
                        column2 = column_data[1]
                        column3 = ''
                    # Save the scraped data to the database
                    table_data = TableData.objects.create(column1=column1, column2=column2, column3=column3)
                    table_data.save()
