import json
from database import get_db_connection

class EthicalAnalyzer:
    def __init__(self, comment_json):
        """
        Initializes an instance of the EthicalAnalyzer class with data from a JSON object.

        :param comment_json: A dictionary containing comment data.
        """
        self.comment_id = comment_json["comment_id"]
        self.event_type = comment_json.get("event_type")
        self.user = comment_json["user"]
        self.user_id = comment_json["user_id"]
        self.user_avatar_url = comment_json.get("user_avatar_url")
        self.user_html_url = comment_json.get("user_html_url")
        self.user_type = comment_json.get("user_type")
        self.comment_body = comment_json["comment_body"]
        self.created_at = comment_json["created_at"]
        self.updated_at = comment_json["updated_at"]
        self.analysis = comment_json.get("analysis", {})
        self.event_number = comment_json.get("event_number")
        self.event_title = comment_json.get("event_title")
        self.event_body = comment_json.get("event_body")
        self.event_url = comment_json.get("event_url")
        self.comment_url = comment_json.get("comment_url")
        self.repository_name = comment_json.get("repository_name")
        self.response_comment = comment_json.get("response_comment")
        self.response_at = comment_json.get("response_at")

    def save_to_db(self):
        """
        Saves the current instance of EthicalAnalyzer to the database.

        The function establishes a connection to the database, ensures the target table exists,
        and inserts the instance's data into the corresponding table.
        """
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Ensure the table for the repository exists
        create_table_if_not_exists()

        # Insert the comment data into the table
        cursor.execute('''
            INSERT INTO comments_analysis (
                comment_id, event_type, user, user_id, user_avatar_url, user_html_url, user_type, comment_body, 
                created_at, updated_at, classification, reasons, numbered_flags, event_number, 
                event_title, event_body, event_url, comment_url, repository_name, response_comment, response_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            self.comment_id,
            self.event_type,
            self.user,
            self.user_id,
            self.user_avatar_url,
            self.user_html_url,
            self.user_type,
            self.comment_body,
            self.created_at,
            self.updated_at,
            self.analysis.get("classification"),
            self.analysis.get("reasons"),
            json.dumps(self.analysis.get("numbered_flags", {})),
            self.event_number,
            self.event_title,
            self.event_body,
            self.event_url,
            self.comment_url,
            self.repository_name,
            self.response_comment,
            self.response_at
        ))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

def create_table_if_not_exists():
    """
    Creates a table for the repository if it does not already exist.
    """
    # Establish a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comment_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            user TEXT NOT NULL,
            user_id TEXT NOT NULL,
            user_avatar_url TEXT,
            user_html_url TEXT,
            user_type TEXT,
            comment_body TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            classification TEXT,
            reasons TEXT,
            numbered_flags TEXT,
            event_number TEXT,
            event_title TEXT,
            event_body TEXT,
            event_url TEXT,
            comment_url TEXT,
            repository_name TEXT,
            response_comment TEXT,
            response_at TEXT
        )
    ''')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
