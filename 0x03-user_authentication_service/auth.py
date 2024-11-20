#!/usr/bin/env python3
"""
authentication module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4

from typing import Union

def _hash_password(password: str) -> str:
    """
    hashes a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
