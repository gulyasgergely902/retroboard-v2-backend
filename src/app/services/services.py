"""All service operations"""

from typing import Optional

from flask import jsonify
from sqlalchemy.exc import DatabaseError

from app.database.database_handler import DatabaseHandler
from app.database.models import Board, Note

db = DatabaseHandler()
db.create_tables()


def get_boards() -> tuple[list[dict[str, str]], int]:
    """Return all boards"""
    with db.get_session() as session:
        boards = session.query(Board).all()

    boards_json = [{"id": board.id, "name": board.name} for board in boards]

    return boards_json, 200


def add_board(board_name: str) -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Add a new board"""
    with db.get_session() as session:
        try:
            session.add(Board(name=board_name))
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500

    return {"status": "Success"}, None, 200


def remove_board(board_id: int) -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Remove a board"""
    with db.get_session() as session:
        try:
            board = session.get(Board, board_id)
            session.delete(board)
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500

    return {"status": "Success"}, None, 200


def get_notes(board_id: int):
    """Return all notes for a board"""
    with db.get_session() as session:
        if board_id is None:
            print("No board id given, returning all notes")
            notes = session.query(Note).all()
        else:
            notes = session.query(Note).where(Note.board_id.is_(board_id))

    notes_json = [{"id": note.id, "description": note.description, "category": note.category, "tags": note.tags} for note in notes]

    return notes_json, 200
