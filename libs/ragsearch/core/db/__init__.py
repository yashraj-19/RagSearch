"""
This module contains the database manager classes.
"""
from .base import BaseDBManager
from .duckdb_manager import DuckDBManager
from .sqlite_manager import SQLiteManager
from .schema_helper import SchemaHelper

__all__ = ["DuckDBManager",
           "SQLiteManager",
           "SchemaHelper"]

class DBManager(BaseDBManager):
    """
    Database manager class for querying the database.
    """
    def __init__(self, data_path, vector_db=None):
        self.db = DuckDBManager(data_path)
        self.vector_db = vector_db  # Reserved for future extension

    def query(self, sql_query):
        """
        Execute a SQL query on the database.
        """
        return self.db.query(sql_query)

    def __str__(self):
        """
        String representation of the DB manager.
        """
        return "DBManager"