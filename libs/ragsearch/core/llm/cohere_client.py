"""
This module provides a client for the Cohere API.
"""
import cohere

class CohereLLM:
    """
    A class to interact with the Cohere API.
    """
    def __init__(self, api_key: str):
        """
        Initialize the Cohere client.

        Args:
            api_key (str): API key for the Cohere API.
        """
        self.client = cohere.Client(api_key)

    def generate(self, prompt: str,
                 model: str = "command-xlarge",
                 max_tokens: int = 100,
                 temperature: float = 0.7) -> str:
        """
        Generate a response using Cohere's LLM.

        Args:
            prompt (str): The input prompt for the LLM.
            model (str): The Cohere model to use.
            max_tokens (int): Maximum tokens in the response.
            temperature (float): Sampling temperature.

        Returns:
            str: The generated response.
        Raises:
            RuntimeError: If the API call fails.
        """
        try:
            response = self.client.generate(
                model=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.generations[0].text.strip()
        except Exception as e:
            raise RuntimeError(f"Cohere API call failed: {e}")

    def __str__(self):
        """
        Return the name of the LLM.
        """
        return "Cohere LLM"