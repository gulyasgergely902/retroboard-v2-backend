"""Routes for RetroBoard Server"""

from flask_restx import Namespace, Resource, reqparse, fields
from flask import request, send_from_directory
from app.services.services import get_boards, add_board, remove_board
from app.services.services import get_notes, add_note, remove_note, modify_note_category, modify_note_tags
from app.services.services import get_categories, add_category, remove_category

boards_ns = Namespace("boards", description="Board related operations")

board_model = boards_ns.model('Board', {
    'name': fields.String(required=True)
})


@boards_ns.route('/')
class Boards(Resource):
    """All boards related endpoints"""

    def get(self):
        """Get all boards"""
        return get_boards()

    @boards_ns.expect(board_model)
    def post(self):
        """Add a new board"""
        data = request.get_json()
        result, error, status = add_board(
            data['name']
        )
        return result or error, status

    def delete(self):
        """Remove a board by id"""
        parser = reqparse.RequestParser()
        parser.add_argument('board_id', type=int)
        args = parser.parse_args()
        result, error, status = remove_board(args['board_id'])
        return result or error, status


notes_ns = Namespace("notes", description="Note related operations")

note_model = notes_ns.model('Note', {
    'description': fields.String(required=True),
    'category': fields.Integer(required=True),
    'tags': fields.List(fields.String, required=False),
    'board_id': fields.Integer(required=True)
})

category_model = notes_ns.model('CategoryUpdate', {
    'category': fields.Integer(required=True, description='New category')
})

tags_model = notes_ns.model('TagsUpdate', {
    'tags': fields.List(fields.String, required=True, description='New tags')
})


@notes_ns.route('/')
class Notes(Resource):
    """All notes related endpoints"""

    def get(self):
        """Get all notes or for a given board"""
        parser = reqparse.RequestParser()
        parser.add_argument('board_id', type=int)
        args = parser.parse_args()
        result, status = get_notes(args['board_id'])
        return result, status

    @notes_ns.expect(note_model)
    def post(self):
        """Add a new note"""
        data = request.get_json()
        result, error, status = add_note(
            data['description'],
            data['category'],
            data.get('tags', []),
            data['board_id'])
        return result or error, status

    def delete(self):
        """Remove a note by id"""
        parser = reqparse.RequestParser()
        parser.add_argument('note_id', type=int)
        args = parser.parse_args()
        result, error, status = remove_note(args['note_id'])
        return result or error, status


@notes_ns.route('/<int:note_id>/category')
class NoteCategoryResource(Resource):
    """Modify a note category"""
    @notes_ns.expect(category_model)
    def put(self, note_id):
        """Update the category of a note"""
        data = request.get_json()
        new_category = data.get('category')

        result, error, status = modify_note_category(note_id, new_category)
        return result or error, status


@notes_ns.route('/<int:note_id>/tags')
class NoteTagsResource(Resource):
    """Modify a note tags"""
    @notes_ns.expect(tags_model)
    def put(self, note_id):
        """Update the tags of a note"""
        data = request.get_json()
        new_tags = data.get('tags')

        result, error, status = modify_note_tags(note_id, new_tags)
        return result or error, status


categories_ns = Namespace(
    "categories", description="Category related operation")

category_model = categories_ns.model('Category', {
    'id': fields.Integer(required=True, description='Category ID'),
    'name': fields.String(required=True),
    'board_id': fields.Integer(required=True)
})


@categories_ns.route('/')
class Categories(Resource):
    """All category related endpoints"""

    def get(self):
        """Get all categories or for a given board"""
        parser = reqparse.RequestParser()
        parser.add_argument('board_id', type=int)
        args = parser.parse_args()
        result, status = get_categories(args['board_id'])
        return result, status

    @notes_ns.expect(category_model)
    def post(self):
        """Add a new category"""
        data = request.get_json()
        result, error, status = add_category(
            data['name'],
            data['board_id']
        )
        return result or error, status

    def delete(self):
        """Delete a category by id"""
        parser = reqparse.RequestParser()
        parser.add_argument('category_id')
        args = parser.parse_args()
        result, error, status = remove_category(args['category_id'])
        return result or error, status


def register_static_routes(app):
    """Register static routes for serving static files"""
    @app.route('/')
    def serve_index():
        """Serve the index page"""
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>')
    def serve_static_file(path):
        """Server static files"""
        return send_from_directory(app.static_folder, path)
