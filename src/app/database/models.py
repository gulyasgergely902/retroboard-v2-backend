"""Database models"""

from typing import List

from sqlalchemy import ForeignKey, String, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.database_handler import Base


class Board(Base):
    """Database model of a Board object"""
    __tablename__ = 'boards'
    __table_args__ = {'sqlite_autoincrement': True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    notes: Mapped[List["Note"]] = relationship(
        back_populates="board", cascade="all, delete-orphan"
    )
    categories: Mapped[List["Category"]] = relationship(
        back_populates="board", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Board(id={self.id!r}, name={self.name!r}, notes={self.notes!r})"


class Note(Base):
    """Database model of a Note"""
    __tablename__ = 'notes'
    __table_args__ = {'sqlite_autoincrement': True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    description: Mapped[str] = mapped_column(String(30))
    category: Mapped[str] = mapped_column(String(30))
    tags: Mapped[list] = mapped_column(JSON)
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))

    board: Mapped["Board"] = relationship(back_populates="notes")

    def __repr__(self) -> str:
        return f"Note(id={self.id!r}, description={self.description!r}, category={self.category!r}, tags={self.tags!r})"


class Category(Base):
    """Database model of  Category"""
    __tablename__ = "categories"
    __table_args__ = {'sqlite_autoincrement': True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    board_id: Mapped[int] = mapped_column(ForeignKey("boards.id"))

    board: Mapped["Board"] = relationship(back_populates="categories")

    def __repr__(self) -> str:
        return f"Category(id={self.id!r}, name={self.name!r})"
