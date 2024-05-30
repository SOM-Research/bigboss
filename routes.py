import logging
from flask import Flask, jsonify
from controllers.ethicanal_controller import analyze

# Initialize the Flask application
app = Flask(__name__)

# Create a logger for this module
logger = logging.getLogger(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_route():
    """
    Flask route for POST requests to /analyze.

    This route calls the analyze function from ethicanal_controller to process and analyze
    the comment data provided in the request.
    
    :return: The response from the analyze function.
    """
    try:
        logger.info("Handling /analyze route")
        return analyze()
    except Exception as e:
        logger.error(f"Error handling /analyze route: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500
