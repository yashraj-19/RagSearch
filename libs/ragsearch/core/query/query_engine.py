"""
Query engine for processing natural language queries into SQL.
"""

from .base import BaseQueryProcessor
from .schema_parser import SchemaParser
from .sql_translator import SQLTranslator


class QueryEngine(BaseQueryProcessor):
    """
    Query engine for processing natural language queries into SQL.
    """

    def __init__(self, db_manager, schema_parser, sql_translator):
        """
        Initializes the QueryEngine with dependencies.

        Args:
            db_manager (BaseDBManager): Database manager for executing SQL.
            schema_parser (SchemaParser): Parses the database schema.
            sql_translator (SQLTranslator): Converts natural language to SQL.
        """
        self.db_manager = db_manager
        self.schema_parser = schema_parser
        self.sql_translator = sql_translator

    def process_query(self, natural_language_query):
        """
        Process a natural language query to retrieve results.

        Args:
            natural_language_query (str): User's input query.

        Returns:
            List[Dict]: Query results from the database.
        """
        # Step 1: Translate natural language to SQL
        sql_query = self.sql_translator.translate(natural_language_query)

        # Step 2: Execute SQL on the database
        results = self.db_manager.query(sql_query)

        return results

    def __str__(self):
        """
        String representation of the query engine.
        """
        return "QueryEngine"
