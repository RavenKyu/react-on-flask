
import logging
from flask import Blueprint
from flask import request, abort, make_response
from flask import jsonify, redirect, url_for, render_template


api = Blueprint('api', __name__, 
                template_folder='templates',
                static_folder='static', 
                static_url_path='assets')


@api.route('/hello', methods=('GET',))
def hello():
    if request.method == 'GET':
        return render_template('index.html')

