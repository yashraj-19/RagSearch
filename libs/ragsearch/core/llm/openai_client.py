"""
This module provides a client for interfacing with OpenAI's language models.
"""
import openai #Importing the openai library

class OpenAILLM:
    """
    A class to interact with OpenAI's language models.
    """
    def __init__(self, api_key: str):
        """
        Initialize the OpenAI client.

        Args:
            api_key (str): API key for the OpenAI API.
        """
        openai.api_key = api_key

    def generate(self, prompt: str,
                 model: str = "gpt-4",
                 max_tokens: int = 100,
                 temperature: float = 0.7) -> str:
        """
        Generate a response using OpenAI's GPT models.

        Args:
            prompt (str): The input prompt for the LLM.
            model (str): The OpenAI model to use.
            max_tokens (int): Maximum tokens in the response.
            temperature (float): Sampling temperature.

        Returns:
            str: The generated response.
        Raises:
            RuntimeError: If the API call fails.
        """
        try:
            response = openai.completions.create(
                model=model,
                prompt=prompt,
                max_tokens=max_tokens,
                temperature=temperature,
            )
            return response.choices[0].text.strip()
        except Exception as e:
            raise RuntimeError(f"OpenAI API call failed: {e}")

    def __str__(self):
        """
        Return the string representation of the client.
        """
        return "OpenAILLM"