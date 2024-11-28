"""
Base class for the LLM manager.
"""
from abc import ABC, abstractmethod


class BaseLLMManager(ABC):
    """
    Abstract class for the LLM manager.
    """
    @abstractmethod
    def generate(self, prompt: str) -> str:
        """Abstract method to generate a response from a given prompt."""
        pass

    def __str__(self) -> str:
        """
        Return the class name as a string.
        """
        return self.__class__.__name__
