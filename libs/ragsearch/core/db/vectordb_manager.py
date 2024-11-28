"""
Vector database manager for managing vector databases.
"""
from .base import BaseDBManager
import pinecone

class VectorDBManager(BaseDBManager):
    """
    Concrete implementation for managing vector databases.
    """

    def __init__(self, api_key, environment="us-west1-gcp"):
        """
        Initialize the vector database manager with API credentials.

        Args:
            api_key (str): The API key for authenticating with the vector database.
            environment (str): The environment to connect to (e.g., "us-west1-gcp").
        """
        pinecone.init(api_key=api_key, environment=environment)
        self.index = None  # Placeholder for the actual index

    def create_index(self, index_name, dimension):
        """
        Create a new vector index.

        Args:
            index_name (str): Name of the vector index.
            dimension (int): Dimensionality of vectors in the index.
        """
        self.index = pinecone.Index(index_name, dimension=dimension)

    def query(self, vector_query, top_k=5):
        """
        Query the vector database and return the top-k results.

        Args:
            vector_query (list): A vector to query against.
            top_k (int): Number of top results to return.

        Returns:
            list: Top-k similar vectors with metadata.
        """
        results = self.index.query(queries=[vector_query], top_k=top_k)
        return results['matches']

    def __del__(self):
        """
        Ensure any resources are cleaned up when the instance is deleted.
        """
        if self.index:
            self.index.close()
