#!/usr/bin/env python3
"""
Route module for the authentication
"""
from flask import Flask, request
from typing import List, TypeVar


class Auth:
    """auth class for authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth method
        """
        return False

    def authorization_header(self, request=None) -> str:
        """authorization_header method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """shows current user"""
        return None
