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
