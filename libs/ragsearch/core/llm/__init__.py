"""
This module provides a class to manage different LLM clients.
"""
from .cohere_client import CohereLLM
from .openai_client import OpenAILLM
from .base import BaseLLMManager

class LLMManager(BaseLLMManager):
    """
    A class to manage different LLM clients.
    """
    def __init__(self, api_key: str, model_name: str):
        """
        Initialize the LLM client based on the model name.

        Args:
            api_key (str): API key for the LLM provider.
            model_name (str): Name of the LLM model to use.
        """
        self.client = self._initialize_client(api_key, model_name)

    def _initialize_client(self, api_key: str, model_name: str):
        """
        Internal method to initialize the appropriate client.

        Args:
            api_key (str): API key for the LLM provider.
            model_name (str): Name of the LLM model.

        Returns:
            BaseLLMManager: Instance of the appropriate LLM client.
        Raises:
            ValueError: If the model name is not supported
        """
        if "cohere" in model_name.lower():
            return CohereLLM(api_key)
        if "gpt" in model_name.lower():
            return OpenAILLM(api_key)
        raise ValueError(f"Unsupported LLM model: {model_name}")

    def generate(self, prompt: str) -> str:
        """
        Generate a response using the underlying LLM client.

        Args:
            prompt (str): The input prompt.

        Returns:
            str: The generated response.
        """
        try:
            return self.client.generate(prompt)
        except Exception as e:
            raise RuntimeError(f"Failed to generate response: {e}")


    def __str__(self):
        """
        Return a string representation of the LLM manager.
        """
        return f"LLMManager(client={self.client})"
