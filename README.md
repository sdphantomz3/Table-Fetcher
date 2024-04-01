# Table Fetcher
 A table fetcher for python (uses django for rendering)

## Working:
It fetches every table from the given url and shows it in the template.

## How to start it?
> First, you need to scrape the data. For that you want to run the following commands:
- python manage.py shell
- from mainapp.scrape import scrape_website_and_save_data
- scrape_website_and_save_data()

> Then, you need to start the django server to view the saved data from scraping.
In your project root type the following command:
- python manage.py runserver 0.0.0.0:[8000]

**You will need basic knowledge of django and python to understand this project.**
