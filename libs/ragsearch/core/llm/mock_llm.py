"""
Mock LLM client for testing purposes.
"""
from .base import BaseLLMManager #Importing the BaseLLMManager class

class MockLLMClient(BaseLLMManager):
    """
    Mock LLM client for testing purposes.
    """
    def generate(self, prompt: str) -> str:
        """
        Generate a mock response for the given prompt.
        """
        return f"Mock response for prompt: {prompt}"

    def __str__(self):
        """
        Return the string representation of the client.
        """
        return "MockLLMClient"
