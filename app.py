from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import make_response
from datetime import datetime
from flask_restful import Resource, Api, reqparse
import time


app = Flask(__name__)
api = Api(app)

urls = [
    {
        'id': 1,
        'long': u'https://example.com/product?ref=01652&type=shirt',
        'short': u'https://tinyurl.com/exampleshirt',
        'date':u''
        #'visits':
    },
    {
        'id': 2,
        'long': u'https://example.com/assets/category_B/subcategory_C/Foo/',
        'short': u'https://example.com/Foo',
        'date': u''
        #'visits':
    }
]

@app.errorhandler(404) #handles error message
def not_found(error):
   return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/urls/', methods=['GET']) #returns a list of all urls
def get_urls():
    return jsonify({'urls': urls})

@app.route('/urls/<int:url_id>', methods=['GET']) #returns url by id
def get_url(url_id):
    url = [url for url in urls if url['id'] == url_id]
    if len(url) == 0:
        abort(404)
    return jsonify({'url': url[0]})


@app.route('/urls', methods=['POST']) #creates a url with the short version and time of creation
def create_url():
    if not request.json or not 'long' in request.json:
        abort(404)
    link = request.json['long']
    t = datetime.now()
    url = {
        'id': urls[-1]['id'] + 1,
        'long': link,
        'short': generate_short_url(link),
        'date': time.strftime("%H:%M:%S", t)
    }
    urls.append(url)

def generate_short_url(self):   #generates a short version of the url
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=3))
        link = self.query.filter_by(short_url=short_url).first()
        if link:
            return self.generate_short_url()
        
        return short_url

@app.route('/urls/<int:url_id>', methods = ['DELETE'])
def delete_url(url_id):
    url = filter(lambda t: t['id'] == url_id, urls)
    if len(url) == 0:
        abort(404)
    urls.remove(url[0])
    return jsonify( { 'result': True } )

