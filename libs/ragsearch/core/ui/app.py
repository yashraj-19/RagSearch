"""
RagSearch UI application
"""
from flask import Flask, request, jsonify

def create_app(query_processor):
    """
    Create a new Flask application.
    """
    app = Flask(__name__)

    @app.route("/query", methods=["POST"])
    def query():
        """
        Handle a query request.
        """
        data = request.json
        query = data["query"]
        results = query_processor.process_query(query)
        return jsonify(results)

    return app
