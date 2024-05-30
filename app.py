import logging
from routes import app

if __name__ == '__main__':
    """
    Entry point for the Flask application.

    This script runs the Flask application, making it listen on all available IP addresses
    on port 5000.
    """
    # Configure logging
    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
    
    app.run(host='0.0.0.0', port=5000)
