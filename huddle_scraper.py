import requests
from bs4 import BeautifulSoup
import time

base_url = "https://huddle.gg/25/playbooks/all-plays/?page={}"
max_pages = 460  # Scrape all 460 pages

for page in range(1, max_pages + 1):
    url = base_url.format(page)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    print(f"\nScraping page {page}: {url}")
    
    # Basic test: Print all play names
    for tag in soup.select('.play-title'):
        print(tag.text.strip())
