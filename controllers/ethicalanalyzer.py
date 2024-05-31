import logging
from flask import request, jsonify
from services.ethicalanalyzer import analyze_and_respond

# Create a logger for this module
logger = logging.getLogger(__name__)

def analyze():
    """
    Flask route handler that processes a POST request to analyze a comment.

    This function extracts the comment JSON from the request, analyzes it using the analyze_and_respond
    function from the ethicanal_service, saves the analysis to the database, and returns the
    analyzed comment JSON as a response.

    :return: A JSON response containing the analyzed comment data and the generated response if applicable.
    """
    try:
        # Log the receipt of a new request
        logger.info("Received request to analyze comment")

        # Extract the JSON payload from the request
        comment_json = request.json
        logger.debug(f"Request JSON: {comment_json}")

        # Analyze the comment and get an EthicAnal object
        ethicanal = analyze_and_respond(comment_json)
        logger.info(f"Comment analyzed: {ethicanal}")

        # Save the analyzed comment to the database
        ethicanal.save_to_db()
        logger.info("Comment saved to database")

        # Return the analyzed comment JSON as a response
        return jsonify(comment_json)
    except Exception as e:
        # Log any exceptions that occur
        logger.error(f"Error analyzing comment: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500
