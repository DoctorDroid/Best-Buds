from os import getenv
from flask import Flask, render_template, request

def create_app():
    # Creating the instance of the application
    app = Flask(__name__)
    DB.init_app(app)

    @app.route('/', methods=['GET', 'POST'] #TODO):
        def parse_request():
            input_data = # the information that they give us


    # TODO figure out where to route these things
    @app.route('/Login'):

    @app.route('/Registration' #TODO):

    @app.route('/Protected'# TODO):

    @app.route()