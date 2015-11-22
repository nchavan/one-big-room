from bone_explorer import app
from flask import request, jsonify
from lib.search import do_search

from lib import specimen

API_URL = '/api'

@app.route(API_URL + '/search')
def search():
    query = request.args.get('query', None)
    group = request.args.get('group', None)
    return jsonify({
            'query': query,
            'results': [
                specimen.get_view_data(),
                specimen.get_view_data(),
                specimen.get_view_data()
                ]
        });

@app.route(API_URL + '/search-test')
def search_test():
    query = request.args.get('query', None)
    group = request.args.get('group', None)
    return jsonify(do_search(query, group))