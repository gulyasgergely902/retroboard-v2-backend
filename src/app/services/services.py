"""All service operations"""

from typing import Optional

from sqlalchemy.exc import DatabaseError
from sqlalchemy import select

from app.database.database_handler import DatabaseHandler
from app.database.models import Board, Note, Category

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


def get_notes(board_id: int) -> tuple[list[dict[str, str]], int]:
    """Return all notes for a board or all"""
    with db.get_session() as session:
        if board_id is None:
            notes = session.query(Note).all()
        else:
            notes = session.query(Note).where(Note.board_id.is_(board_id))

    notes_json = [{"id": note.id, "description": note.description, "category": note.category, "tags": note.tags} for note in notes]

    return notes_json, 200


def add_note(note_description: str, note_category: str, note_tags: str, note_board_id: int)  -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Add a new note"""
    with db.get_session() as session:
        try:
            session.add(Note(
                description=note_description,
                category=note_category,
                tags=note_tags,
                board_id=note_board_id
            ))
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500
    return {"status": "Success"}, None, 200


def remove_note(note_id: int) -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Remove a note"""
    with db.get_session() as session:
        try:
            note = session.get(Note, note_id)
            session.delete(note)
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500
    return {"status": "Success"}, None, 200


def modify_note_category(note_id: int, new_category: str) -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Modify a note category by id"""
    with db.get_session() as session:
        try:
            statement = select(Note).where(Note.id == note_id)
            note = session.scalars(statement).one()
            note.category = new_category
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500
    return {"status": "Success"}, None, 200


def modify_note_tags(note_id: int, new_tags: list) -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Modify a note category by id"""
    with db.get_session() as session:
        try:
            statement = select(Note).where(Note.id == note_id)
            note = session.scalars(statement).one()
            note.tags = new_tags
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500
    return {"status": "Success"}, None, 200


def get_categories(board_id: int) -> tuple[list[dict[str, str]], int]:
    """Return all categories for a board or all"""
    with db.get_session() as session:
        if board_id is None:
            categories = session.query(Category).all()
        else:
            categories = session.query(Category).where(Category.board_id.is_(board_id))

    categories_json = [{"id": category.id, "name": category.name} for category in categories]

    return categories_json, 200


def add_category(category_name: str, category_board_id: int) -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Add a new category"""
    with db.get_session() as session:
        try:
            session.add(Category(
                name=category_name,
                board_id=category_board_id
            ))
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500
    return {"status": "Success"}, None, 200


def remove_category(category_id: int) -> tuple[Optional[dict[str, str]], Optional[dict[str, str]], int]:
    """Remove a category"""
    with db.get_session() as session:
        try:
            category = session.get(Category, category_id)
            session.delete(category)
            session.commit()
        except DatabaseError as e:
            return None, {"status": f"DB Error: {e}"}, 500
    return {"status": "Success"}, None, 200
