"""
Utility class to inspect and manage the database schema.
"""

class SchemaHelper:
    """
    Utility class to inspect and manage the database schema.
    """

    @staticmethod
    def get_table_info(db_manager, table_name):
        """
        Get column names for a given table.

        Args:
            db_manager (BaseDBManager): The database manager instance.
            table_name (str): The name of the table.

        Returns:
            list: A list of column names.

        Raises:
            ValueError: If the database manager or table name is not provided.
        """
        if not db_manager:
            raise ValueError("Database manager is not provided.")
        if not table_name:
            raise ValueError("Table name is not provided.")
        sql_query = f"PRAGMA table_info({table_name})"  # SQLite-specific; modify for other DBs
        columns = db_manager.query(sql_query)
        return [column[1] for column in columns]  # Assuming column[1] is the column name in SQLite

    def __str__(self):
        """
        String representation of the schema helper.
        """
        return "SchemaHelper"
