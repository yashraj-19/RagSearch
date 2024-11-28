from libs.ragsearch.core.llm import LLMManager
from libs.ragsearch.core.llm.mock_llm import MockLLMClient
import pytest

def test_llm_manager_with_cohere_mock():
    """
    Test the LLM manager with the Cohere mock client.
    """
    manager = LLMManager(api_key="fake_key", model_name="cohere-mock")
    manager.client = MockLLMClient()  # Replace actual client with mock
    response = manager.generate("Test prompt")
    assert response == "Mock response for prompt: Test prompt"

def test_llm_manager_with_openai_mock():
    """
    Test the LLM manager with the OpenAI mock client.
    """
    manager = LLMManager(api_key="fake_key", model_name="gpt-mock")
    manager.client = MockLLMClient()  # Replace actual client with mock
    response = manager.generate("Test prompt")
    assert response == "Mock response for prompt: Test prompt"
