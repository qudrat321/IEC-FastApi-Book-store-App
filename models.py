# Import the shared base class used to define database tables.
from db import Base

# Import the tools used to describe table columns and the kinds of values they hold.
from SQLAlchemy import Column, Integer, String, Float, DateTime


# This class describes the book information stored in the database.
class Book(Base):
    # Use "Books" as the name of the database table.
    __tablename__ = "Books"

    # A unique number used to identify each book.
    id = Column(Integer, primary_key=True, index=True)

    # The book's title.
    title = Column(String, index=True)

    # A short description of the book.
    description = Column(String, index=True)

    # The book author's information.
    author = Column(Integer, index=True)

    # The year the book was published.
    year = Column(Integer, index=True)