

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin  # Import urljoin function for resolving relative URLs

# URL of the specific page to scrape
url = 'https://www.lboro.ac.uk/study/postgraduate/masters-degrees/january-start/a-z/'


# Function to scrape links from the specific page
def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the specific section containing links
        section = soup.find('ul', class_='list list--degrees js-degrees-list')  # Adjust class name accordingly
        if section:
            # Find and extract links within the section
            links = section.find_all('a', href=True)
            for link in links:
                # Resolve relative URLs to absolute URLs
                absolute_url = urljoin(url, link['href'])
                print(absolute_url)  # or store the links in a list or file
        else:
            print('Specific section not found on page:', url)
    else:
        print('Error scraping page:', response.status_code)

# Scrape links from the specific page
scrape_page(url)

