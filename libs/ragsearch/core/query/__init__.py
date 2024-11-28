"""
Query processing module for ragsearch
"""

from .base import BaseQueryProcessor
from .query_engine import QueryEngine
from .schema_parser import SchemaParser
from .sql_translator import SQLTranslator

__all__ = [
    "BaseQueryProcessor",
    "QueryEngine",
    "SchemaParser",
    "SQLTranslator"
]

class QueryProcessor(BaseQueryProcessor):
    """
    Query processor class for handling natural language queries.
    """
    def __init__(self, llm, db):
        """
        Initialize the query processor with LLM and DB managers.
        """
        self.llm = llm
        self.db = db
        self.sql_translator = SQLTranslator(llm)

    def process_query(self, natural_language_query):
        """
        Process a natural language query and return results.
        """
        sql_query = self.sql_translator.translate(natural_language_query)
        return self.db.query(sql_query)
