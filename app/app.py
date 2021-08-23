from flask import Flask
from app.api.v1.api import api
from app.web.app import web

app = Flask(__name__)

app.register_blueprint(web, url_prefix='/')
app.register_blueprint(api, url_prefix='/api/v1')


