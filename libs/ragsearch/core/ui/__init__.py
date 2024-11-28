"""
RAGSearch web application runner.
"""
from .app import create_app

class WebApp:
    """
    Web application runner for RAGSearch.
    """
    def __init__(self, query_processor):
        """
        Initialize the web application runner.
        """
        self.query_processor = query_processor

    def launch(self):
        """
        Launch the web application.
        """
        app = create_app(self.query_processor)
        app.run(host="0.0.0.0", port=8080)
