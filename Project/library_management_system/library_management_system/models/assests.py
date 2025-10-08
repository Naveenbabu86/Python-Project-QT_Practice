"""This module will have necessary library assets
"""
from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class LibraryItem:
    """Represents an item in the library catalog.

    Attributes:
        id (str): Unique identifier for the library item.
        title (str): Title of the item.
        author (str): Author or creator of the item.
        isbn (Optional[str]): International Standard Book Number, if available.
        publisher (Optional[str]): Name of the publisher, if available.
        category (Optional[str]): Category or genre of the item, if specified.
        type: Type of library item can be among Books, Dvds...
    """
    id: str
    title: str
    author: str
    isbn: Optional[str] = None
    publisher: Optional[str] = None
    category: Optional[str] = None
    type: str = 'Book'

# todo:
@dataclass
class Contact:
    """Represents a contact person associated with the library.

    Attributes:
        name (str): Name of the contact person.
        phoneno (str): Contact phone number.
        address (str): Contact address.
        email (Optional[str]): Email address of the contact.
        contact_type (str): Type of contact ('Member', 'Staff', 'Supplier', etc.).
        date_of_birth (Optional[date]): Date of birth (if applicable).
        membership_id (Optional[str]): Unique membership ID for library members.
        join_date (Optional[date]): Date when the contact joined the library system.
        is_active (bool): Whether the contact is currently active in the system.
    """
    name: str
    phoneno: str
    address: str
    email: Optional[str] = None
    contact_type: str = 'Member'
    date_of_birth: Optional[date] = None
    membership_id: Optional[str] = None
    join_date: Optional[date] = None
    is_active: bool = True

