"""
This module contains the SchemaParser class which is
responsible for parsing and understanding the database schema.
"""

class SchemaParser:
    """
    Parses and understands the database schema.
    """

    def __init__(self, schema):
        """
        Initialize with the database schema.

        Args:
            schema (Dict): The database schema metadata.
        """
        self.schema = schema

    def get_table_info(self):
        """
        Retrieve metadata about tables and their columns.

        Returns:
            Dict: Table and column details.
        """
        return self.schema

    def __str__(self):
        """
        String representation of the schema parser.
        """
        return "SchemaParser"
