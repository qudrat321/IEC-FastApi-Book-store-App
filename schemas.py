"""Define the data shapes used to receive and return book information."""

from pydantic import BaseModel


class BookBase(BaseModel):
    """Common book details used when validating book data.

    Expected input: A title, description, author, and publication year.
    Output: A Pydantic model containing validated book details.
    Why it is needed: Gives create and response schemas the same basic fields.
    """

    title: str
    description: str   
    author: str
    year: int


class BookCreate(BookBase):
    """Describe book details accepted when creating a book.

    Expected input: A title, description, author, and publication year.
    Output: A validated book-creation model without an ID.
    Why it is needed: The database assigns an ID after the book is created.
    """

    pass


class Book(BookBase):
    """Describe the book data returned with its database ID.

    Expected input: The common book details and an integer ID.
    Output: A validated book model suitable for returning to a caller.
    Why it is needed: Represents a saved book, including its assigned ID.
    """

    id: int

    class Config:
        # Allow Pydantic to read values from database model objects.
        orm_mode = True
        from_attributes = True
