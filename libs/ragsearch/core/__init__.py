"""
RagSearch Core Module
"""
from pathlib import Path
from ragsearch.core.llm import LLMManager
from ragsearch.core.db import BaseDBManager, DuckDBManager, SQLiteManager
from ragsearch.core.query import (
    QueryEngine,
    SchemaParser,
    SQLTranslator,
)


class RAGSearchEngine:
    """
    Main entry point for the RAG engine. Orchestrates LLM, database, and query modules.
    """

    def __init__(self, data_path: Path, llm_api_key: str, llm_model_name: str):
        # Initialize LLM Manager
        self.llm_manager = LLMManager(api_key=llm_api_key, model_name=llm_model_name)

        # Initialize Database Manager
        self.db_manager = DuckDBManager(data_path)

        # Initialize Query Engine
        schema_parser = SchemaParser(self.db_manager)
        sql_translator = SQLTranslator(self.llm_manager)
        self.query_engine = QueryEngine(self.db_manager, schema_parser, sql_translator)

    def query(self, natural_language_query: str):
        """
        Process a natural language query and return results.
        """
        return self.query_engine.process_query(natural_language_query)

    def run(self):
        """
        Launch a simple web app for querying.
        """
        from ragsearch.core.app_runner import AppRunner
        app = AppRunner(self)
        app.run()


def setup(data_path: Path, llm_api_key: str, llm_model_name: str) -> RAGSearchEngine:
    """
    Factory function for creating a RAGEngine instance.
    """
    return RAGSearchEngine(data_path=data_path, llm_api_key=llm_api_key, llm_model_name=llm_model_name)
