"""Entrypont for RetroBoard server"""

from flask import Flask
from flask_restx import Api
from app.routes.board_routes import boards_ns, notes_ns, categories_ns


def create_app():
    """Create RetroBoard Flask Server"""
    app = Flask(__name__)
    api = Api(app, version='1.0', title='RetroBoard V2',
              description='RetroBoard V2')

    api.add_namespace(boards_ns)
    api.add_namespace(notes_ns)
    api.add_namespace(categories_ns)

    return app
