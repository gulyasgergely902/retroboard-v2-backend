"""Entrypont for RetroBoard server"""

import os
from flask import Flask
from flask_restx import Api
from app.routes.board_routes import boards_ns, notes_ns, categories_ns


def create_app():
    """Create RetroBoard Flask Server"""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(root_dir, 'static')

    app = Flask(__name__, static_folder=static_dir, static_url_path='')
    api = Api(app, version='1.0', title='RetroBoard V2',
              description='RetroBoard V2', doc='/api/docs',
              prefix='/api')

    api.add_namespace(boards_ns)
    api.add_namespace(notes_ns)
    api.add_namespace(categories_ns)

    return app
