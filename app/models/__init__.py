# ======================
# app/models/__init__.py
# ======================

# --- Imports ---
from .db import get_db_connection

__all__ = ["get_db_connection"]