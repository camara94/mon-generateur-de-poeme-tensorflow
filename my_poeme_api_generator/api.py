# -*- coding: utf-8 -*-
from os import abort
from urllib import response
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask_cors import CORS
from flask_cors import cross_origin

from poeme_gen_model import *

app = Flask(__name__)
cors = CORS(app)


@app.route('/', methods=['GET'])
@cross_origin()
def accueil():
    return render_template("index.html")


@app.route('/api/words', methods=['GET'])
def word_index():
    return jsonify({
        'status': 'ok',
        'poeme': get_word_index()
    })


@app.route('/api/poemes', methods=['GET'])
@cross_origin()
def resume_auto():
    if 'tag' in request.args:
        tag = str(request.args['tag'])
        return generer_poeme(seed_text=tag)[len(tag):]
    else:
        return "Erreur: il n' ya pas de paramètre url"


@app.route('/api/poeme', methods=['POST'])
@cross_origin()
def poeme():
    if not request.json or not 'tag' in request.json:
        abort(404)
    else:
        response = generer_poeme(request.json['tag'])
    return jsonify({
        'status': 'ok',
        'poeme': response
    })


if __name__ == "__main__":
    app.run(debug=True)
