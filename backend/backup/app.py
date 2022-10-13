from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app=app, version='1.0', title='Games List', description='Games List', doc='/doc/')
