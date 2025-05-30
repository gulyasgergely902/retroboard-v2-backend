"""Routes for RetroBoard Server"""

from flask_restx import Namespace, Resource, reqparse
from app.services.services import get_boards, add_board, remove_board, get_notes

boards_ns = Namespace("boards", description="Board related operations")
notes_ns = Namespace("notes", description="Note related operations")


@boards_ns.route('/')
class Boards(Resource):
    """All boards related endpoints"""
    def get(self):
        """Getting the existing boards"""
        return get_boards()

    def post(self):
        """Adding new board"""
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str)
        args = parser.parse_args()
        result, error, status = add_board(args['name'])
        return result or error, status

    def delete(self):
        """Remove a board by id"""
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        result, error, status = remove_board(args['id'])
        return result or error, status


@notes_ns.route('/')
class Notes(Resource):
    """All notes related endpoints"""
    def get(self):
        """Get all notes for a given board"""
        parser = reqparse.RequestParser()
        parser.add_argument('board_id', type=int)
        args = parser.parse_args()
        result, status = get_notes(args['board_id'])
        return result, status
