"""Database handler"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

Base = declarative_base()


class DatabaseHandler:
    """Main class for database handling"""
    def __init__(self, db_url='sqlite:///data.sqlite'):
        self.engine = create_engine(db_url, echo=False)
        self.session_local = sessionmaker(bind=self.engine)

    def create_tables(self):
        """Create new database tables"""
        Base.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        """Get database session"""
        return self.session_local()
