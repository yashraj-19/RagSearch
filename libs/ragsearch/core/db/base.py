"""
Base class for all database managers
"""

from abc import ABC, abstractmethod

class BaseDBManager(ABC):
    """
    Base class for all database managers
    """

    @abstractmethod
    def query(self, sql_query):
        """
        Execute a SQL query on the database.
        """
        pass

    def __str__(self):
        """
        String representation of the database manager.
        """
        return "BaseDBManager"
