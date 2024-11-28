"""
Base class for query processors.
"""

from abc import ABC, abstractmethod

class BaseQueryProcessor(ABC):
    """
    Abstract class for query processors.
    """

    @abstractmethod
    def process_query(self, natural_language_query):
        """
        Abstract method to process a natural language query.
        """
        pass

    def __str__(self) -> str:
        """
        Return the class name as a string.
        """
        return self.__class__.__name__

