from flask import Flask, request
from flask_restful import Resource, Api
from ddot import controller
from ddot.controller import Controller

app = Flask(__name__)
api = Api(app)

api.add_resource(Controller, '/cd')
app.run()