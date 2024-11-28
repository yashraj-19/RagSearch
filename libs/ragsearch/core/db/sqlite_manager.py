"""
SQLite database manager.
"""

import sqlite3
import pandas as pd
from .base import BaseDBManager


class SQLiteManager(BaseDBManager):
    """
    Database manager for SQLite.
    """

    def __init__(self, db_path: str = ":memory:"):
        """
        Initialize the SQLite connection.

        :param db_path: Path to the SQLite file (":memory:" for in-memory database).
        """
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row

    def query(self, sql_query: str):
        """
        Execute a SQL query on the SQLite database.

        :param sql_query: The SQL query to execute.
        :return: Query results as a pandas DataFrame.
        """
        cursor = self.connection.execute(sql_query)
        rows = cursor.fetchall()
        return pd.DataFrame([dict(row) for row in rows])

    def load_table(self, data, table_name: str):
        """
        Load data into SQLite as a table.

        :param data: A pandas DataFrame or path to a CSV file.
        :param table_name: Name of the table to create in SQLite.
        """
        if isinstance(data, str):
            df = pd.read_csv(data)
            df.to_sql(table_name, self.connection, if_exists="replace", index=False)
        else:
            data.to_sql(table_name, self.connection, if_exists="replace", index=False)

    def __str__(self):
        """
        String representation of SQLite manager.
        """
        return "SQLiteManager"
