from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True

books = [
    {
        'id': 0,
        'title': 'A Fire Upon the Deep',
        'author': 'Vernor Vinge',
        'first sentence': 'The coldsleep itself was dreamless.',
        'published': '1992'
    },
    {
        'id': 1,
        'title': 'The Ones Who Walk Away From Omelan',
        'author': 'Ursula K. Le Guin',
        'first sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
        'published': '1973'
    },
    {
        'id': 2,
        'title': 'Dhalgren',
        'author': 'Samuel R. Delany',
        'first sentence': 'to wound the autumnal city.',
        'published': '1975'
    }
]

@app.route('/', methods=['GET'])
def home():
    return '<h1>Distant Reading Archive</h1><p>A prototype API for distant reading of science fiction novels.</p>'

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. Please specify an id."

    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    return jsonify(results)

if __name__ == '__main__':
    app.run()

