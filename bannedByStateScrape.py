import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.harpersbazaar.com/culture/a45012950/banned-book-list/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

data = []

current_state = None

for div in soup.find_all('div', class_='css-1pmfua e1u56cep0'):
    if div.find('p'):
        current_state = div.find('p').get_text().strip()

    for p in div.find_all('p', class_='css-106f026 et3p2gv0'):
        if p.find('a') and p.find('a').find('em'):
            title = p.find('a').find('em').get_text()
            author = p.get_text().split(',')[-1].strip()
            data.append({'state': current_state, 'title': title, 'author': author})

# Save the data as a JSON file
with open('scraped_data.json', 'w') as f:
    json.dump(data, f, indent=4)