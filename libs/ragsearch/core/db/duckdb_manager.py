"""
DuckDB database manager.
"""
import duckdb
from .base import BaseDBManager

class DuckDBManager(BaseDBManager):
    """
    Database manager for DuckDB.
    """

    def __init__(self, db_path: str = ":memory:"):
        """
        Initialize the DuckDB connection.

        :param db_path: Path to the DuckDB file (":memory:" for in-memory database).
        """
        self.connection = duckdb.connect(database=db_path, read_only=False)

    def query(self, sql_query: str):
        """
        Execute a SQL query on the DuckDB database.

        :param sql_query: The SQL query to execute.
        :return: Query results as a pandas DataFrame.
        """
        return self.connection.execute(sql_query).fetchdf()

    def load_table(self, data, table_name: str):
        """
        Load data into DuckDB as a table.

        :param data: A pandas DataFrame or path to a file (CSV/Parquet).
        :param table_name: Name of the table to create in DuckDB.
        """
        if isinstance(data, str):
            self.connection.execute(f"CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto('{data}')")
        else:
            self.connection.register(table_name, data)

    def __str__(self):
        """
        String representation of DuckDB manager.
        """
        return "DuckDBManager"
