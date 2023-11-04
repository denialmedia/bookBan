from flask import Flask, jsonify, request
import json
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
# Load the JSON data
with open('enriched_data.json', 'r') as f:
    enriched_data = json.load(f)

# Endpoint for states to return books banned in that state
@app.route('/states', methods=['GET'])
def get_books_by_state():
    query = request.args.get('q')
    if query:
        books = [entry for entry in enriched_data if entry['state'].lower() == query.lower()]
    else:
        books = enriched_data
    return jsonify({'books': books})

# Endpoint to get all available states
@app.route('/states/all', methods=['GET'])
def get_all_states():
    states = list(set(entry['state'] for entry in enriched_data))
    return jsonify({'states': states})

# Endpoint to get all available genres
@app.route('/genres', methods=['GET'])
def get_genres():
    genres = list(set(entry['genre'] for entry in enriched_data))
    return jsonify({'genres': genres})

# Endpoint for search
@app.route('/search/<query>', methods=['GET'])
def search(query):
    results = [entry for entry in enriched_data if query.lower() in entry['title'].lower()]
    return jsonify({'results': results})

# Endpoint to get all books
@app.route('/all', methods=['GET'])
def get_all():
    return jsonify({'data': enriched_data})

# Endpoint to get books with a rating higher than a given value
@app.route('/rating/<min_rating>', methods=['GET'])
def get_rating(min_rating):
    results = [entry for entry in enriched_data if float(entry['rating']) >= float(min_rating)]
    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)