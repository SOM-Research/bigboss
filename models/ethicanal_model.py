import json
from database import get_db_connection

class EthicAnal:
    def __init__(self, comment_json):
        """
        Initializes an instance of the EthicAnal class with data from a JSON object.

        :param comment_json: A dictionary containing comment data.
        """
        self.comment_id = comment_json["comment_id"]
        self.user = comment_json["user"]
        self.user_id = comment_json["user_id"]
        self.comment_body = comment_json["comment_body"]
        self.created_at = comment_json["created_at"]
        self.updated_at = comment_json["updated_at"]
        self.analysis = comment_json.get("analysis", {})
        self.issue_number = comment_json.get("issue_number")
        self.issue_title = comment_json.get("issue_title")
        self.issue_body = comment_json.get("issue_body")
        self.issue_url = comment_json.get("issue_url")
        self.comment_url = comment_json.get("comment_url")
        self.repository_name = comment_json.get("repository_name")
        self.repository_full_name = comment_json.get("repository_full_name")
        self.repository_html_url = comment_json.get("repository_html_url")

    def save_to_db(self):
        """
        Saves the current instance of EthicAnal to the database.

        The function establishes a connection to the database, ensures the target table exists,
        and inserts the instance's data into the corresponding table.
        """
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Replace slashes in repository name to create a valid table name
        repo_name = self.repository_name.replace("/", "_")

        # Ensure the table for the repository exists
        create_table_if_not_exists(repo_name)

        # Insert the comment data into the table
        cursor.execute(f'''
            INSERT INTO {repo_name} (
                comment_id, user, user_id, comment_body, created_at, updated_at, 
                classification, reasons, numbered_flags,
                issue_number, issue_title, issue_body, issue_url, 
                comment_url, repository_name, repository_full_name, repository_html_url
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            self.comment_id,
            self.user,
            self.user_id,
            self.comment_body,
            self.created_at,
            self.updated_at,
            self.analysis.get("classification"),
            self.analysis.get("reasons"),
            json.dumps(self.analysis.get("numbered_flags", {})),
            self.issue_number,
            self.issue_title,
            self.issue_body,
            self.issue_url,
            self.comment_url,
            self.repository_name,
            self.repository_full_name,
            self.repository_html_url
        ))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

def create_table_if_not_exists(repo_name):
    """
    Creates a table for the repository if it does not already exist.

    :param repo_name: The name of the repository, used to name the table.
    """
    # Establish a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {repo_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            comment_id TEXT NOT NULL,
            user TEXT NOT NULL,
            user_id TEXT NOT NULL,
            comment_body TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            classification TEXT NOT NULL,
            reasons TEXT NOT NULL,
            numbered_flags TEXT NOT NULL,
            issue_number TEXT,
            issue_title TEXT,
            issue_body TEXT,
            issue_url TEXT,
            comment_url TEXT,
            repository_name TEXT,
            repository_full_name TEXT,
            repository_html_url TEXT
        )
    ''')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
