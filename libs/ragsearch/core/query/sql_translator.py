"""
SQL Translator module for translating natural language queries to SQL.
"""

class SQLTranslator:
    """
    Translates natural language queries to SQL.
    """

    def __init__(self, llm_manager):
        """
        Initialize with an LLM manager for natural language processing.

        Args:
            llm_manager (BaseLLMManager): LLM client for translation tasks.
        """
        self.llm_manager = llm_manager

    def translate(self, natural_language_query):
        """
        Translate natural language query to SQL using the LLM.

        Args:
            natural_language_query (str): User's query.

        Returns:
            str: Generated SQL query.
        """
        # Prompt LLM for SQL translation
        prompt = f"Translate the following natural language query to SQL:\n{natural_language_query}"
        return self.llm_manager.generate(prompt)
