import logging
import os
from flask import Blueprint, request
from flask import request, abort, make_response, send_from_directory
from flask import jsonify, redirect, url_for, render_template
from jinja2 import TemplateNotFound


web = Blueprint('web', __name__, static_folder='app', static_url_path='web/app', template_folder='app')


@web.route('/', defaults={'path': 'index.html'})
@web.route('/<path:path>')
def source(path):
    if path == 'index.html' or path == 'login':
        return render_template('index.html')
    try:
        return web.send_static_file(path)
    except Exception as e:
        return render_template('index.html')    
    # return send_from_directory('web/app', path)







