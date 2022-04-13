# -*- coding: utf-8 -*-
from os import abort
from urllib import response
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import json
from flask_cors import CORS
from poeme_gen_model import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def accueil():
    return render_template("index.html")


@app.route('/api/words', methods=['GET'])
def word_indx():
    return jsonify({
        'status': 'ok',
        'poeme': get_word_index()
    })


@app.route('/api/poemes', methods=['POST'])
def poeme():
    if not request.json or not 'tag' in request.json:
        abort(404)
    else:
        response = generer_poeme(request.json['tag'])

    return jsonify({
        'status': 'ok',
        'poeme': response[len(request.json['tag'])+1:]
    })


if __name__ == "__main__":
    app.run(debug=True)
