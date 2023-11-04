import requests
import json

# Load the data from the JSON file
with open('scraped_data.json', 'r') as f:
    data = json.load(f)

# Function to get book details from Google Books API
def get_book_details(title, author):
    print(f"Searching for details of {title} by {author}...")
    url = f'https://www.googleapis.com/books/v1/volumes?q={title}+inauthor:{author}'
    response = requests.get(url)
    if response.status_code == 200:
        items = response.json().get('items')
        if items:
            print(f"Details found for {title} by {author}!")
            item = items[0]
            volume_info = item.get('volumeInfo', {})
            industry_identifiers = volume_info.get('industryIdentifiers', [])
            isbn = next((i['identifier'] for i in industry_identifiers if i['type'] == 'ISBN_13'), 'N/A') if industry_identifiers else 'N/A'
            return {
                'description': volume_info.get('description', 'N/A'),
                'genre': volume_info.get('categories', 'N/A'),
                'published_date': volume_info.get('publishedDate', 'N/A'),
                'rating': volume_info.get('averageRating', 'N/A'),
                'cover_link': volume_info.get('imageLinks', {}).get('thumbnail', 'N/A'),
                'isbn': isbn
            }
    print(f"No details found for {title} by {author}.")
    return None
# Update data with additional details
updated_data = []
for idx, item in enumerate(data):
    print(f"Processing book {idx + 1} out of {len(data)}")
    book_details = get_book_details(item['title'], item['author'])
    if book_details:
        item.update(book_details)
    updated_data.append(item)

# Save the updated data as a new JSON file
with open('enriched_data.json', 'w') as f:
    json.dump(updated_data, f, indent=4)

print("Enriched data saved in enriched_data.json")