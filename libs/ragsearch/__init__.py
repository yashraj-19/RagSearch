from ragsearch.core.llm import LLMManager
from ragsearch.core.db import DBManager
from ragsearch.core.query import QueryProcessor
from ragsearch.core.ui import WebApp
from abc import ABC, abstractmethod

class BaseEngine(ABC):

    @abstractmethod
    def query(self, natural_language_query):
        pass

    @abstractmethod
    def run(self):
        pass

class RAG(BaseEngine):
    """
    Main entry point for the RAG engine. Orchestrates LLM, database, and query modules.
    """
    def __init__(self, data_path, llm_api_key, llm_model_name, vector_db=None):
        self.data_path = data_path
        self.llm = LLMManager(api_key=llm_api_key, model_name=llm_model_name)
        self.db = DBManager(data_path=data_path, vector_db=vector_db)
        self.query_processor = QueryProcessor(self.llm, self.db)
        self.web_app = WebApp(self.query_processor)

    def query(self, natural_language_query):
        """
        Process a natural language query and return results.
        """
        return self.query_processor.process_query(natural_language_query)

    def run(self):
        """
        Launch a simple web app for querying.
        """
        self.web_app.launch()

def setup(data_path, llm_api_key, llm_model_name, vector_db=None):
    """
    Factory function for creating a RAGEngine instance.
    """
    return RAG(data_path, llm_api_key, llm_model_name, vector_db)
