import logging
from flask import request, jsonify
from services.ethicalanalyzer import analyze_and_respond

# Create a logger for this module
logger = logging.getLogger(__name__)

def analyze():
    """
    Flask route handler that processes a POST request to analyze a comment or code of conduct.

    :return: A JSON response containing the analyzed data.
    """
    try:
        # Log the receipt of a new request
        logger.info("Received request to analyze payload")

        # Extract the JSON payload from the request
        payload = request.json
        logger.debug(f"Request JSON: {payload}")

        # Check the type of the payload
        payload_type = payload.get('type')
        if not payload_type:
            raise ValueError("Payload type is not specified")

        # Handle the payload based on its type
        if payload_type == 'comment':
            return analyze_comment(payload.get('data'))
        elif payload_type == 'code_of_conduct':
            return analyze_code_of_conduct(payload.get('data'))
        else:
            raise ValueError(f"Unknown payload type: {payload_type}")

    except Exception as e:
        # Log any exceptions that occur
        logger.error(f"Error processing payload: {e}", exc_info=True)
        return jsonify({"error": str(e)}), 500

def analyze_comment(comment_json):
    """
    Analyzes a comment payload.

    :param comment_json: The comment data in JSON format.
    :return: A JSON response containing the analyzed comment data.
    """
    if not comment_json:
        raise ValueError("No comment data provided")
    ethicanal = analyze_and_respond(comment_json)
    logger.info(f"Comment analyzed: {ethicanal}")
    ethicanal.save_to_db()
    logger.info("Comment saved to database")
    return jsonify(comment_json)

def analyze_code_of_conduct(code_of_conduct_text):
    """
    Analyzes a code of conduct payload.

    :param code_of_conduct_text: The code of conduct data in text format.
    :return: A JSON response confirming receipt and saving of the code of conduct.
    """
    if not code_of_conduct_text:
        raise ValueError("No code of conduct data provided")
    # Process and save the code of conduct
    with open('code_of_conduct_received.md', 'w') as file:
        file.write(code_of_conduct_text)
    logger.info("Code of Conduct received and saved")
    return jsonify({"message": "Code of Conduct received", "data": code_of_conduct_text})
