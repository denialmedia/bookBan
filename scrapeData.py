from newsapi import NewsApiClient
import json

# Initialize News API client
newsapi = NewsApiClient(api_key='0edbb8ebe511441cbb393b04d2f68e0d')

# Define search query for banned books in the US
query = 'banned books in US'

# Fetch news articles based on the search query
articles = newsapi.get_everything(q=query, language='en', page_size=100)

# Store relevant information in a list of dictionaries
banned_books_list = []

for article in articles['articles']:
    banned_books_list.append({
        'title': article['title'],
        'description': article['description'],
        'url': article['url'],
        'publishedAt': article['publishedAt']
    })

# Save data as a JSON file
with open('banned_books.json', 'w') as json_file:
    json.dump(banned_books_list, json_file, indent=4)

print("Data successfully saved as banned_books.json")