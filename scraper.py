import requests
from bs4 import BeautifulSoup

def scrape_website(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.string

    paragraphs = soup.find_all('p')

    with open('data.txt', 'w', encoding='utf-8') as file:

        file.write("WEBSITE TITLE:\n")
        file.write(title + "\n\n")

        file.write("PARAGRAPHS:\n")

        for p in paragraphs[:10]:
            
            file.write(p.get_text() + "\n\n")
