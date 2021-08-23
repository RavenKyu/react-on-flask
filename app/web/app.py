import logging
import os
from flask import Blueprint, request
from flask import request, abort, make_response, send_from_directory
from flask import jsonify, redirect, url_for, render_template
from jinja2 import TemplateNotFound


web = Blueprint('web', __name__, 
                template_folder='app',
                static_folder='app')

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/app', defaults={'path': 'index.html'})
@web.route('/app/<path:path>')
def source(path):
    print(url_for('static_folder'))
    return send_from_directory('', path)







