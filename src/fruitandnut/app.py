from flask import Flask
from flask import Response
from flask import request

import json

from .fruit import Fruit

app = Flask(__name__)

fruits = []

@app.before_first_request
def build_fruits():
    fruits.append(Fruit('Banana', 'Tropical fruit'))
    fruits.append(Fruit('Apple', 'Winter fruit'))
   
@app.route('/fruits', methods=['GET'])
def list_fruits():
    return Response(json.dumps([ f.__dict__ for f in fruits ]), mimetype="application/json")

@app.route('/fruits', methods=['POST'])
def post_fruit():
    fruit_json = request.get_json()
    fruits.append(Fruit(**fruit_json))
    return ""
  
@app.route('/fruits', methods=['DELETE'])
def delete_fruit():
    fruit_json = request.get_json()
    target_fruit = Fruit(**fruit_json)
    fruits.remove(target_fruit)
    return ""
