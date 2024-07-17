import json
from database import get_db_connection

class CodeOfConductAnalyzer:
    def __init__(self, coc_analysis_json):
        """
        Initializes an instance of the CodeOfConductAnalyzer class with data from a JSON object.

        :param coc_analysis_json: A dictionary containing the Code of Conduct analysis data.
        """
        self.repository_name = coc_analysis_json["repository_name"]
        self.repository_url = coc_analysis_json["repository_url"]
        self.analyzed_at = coc_analysis_json["analyzed_at"]
        self.code_of_conduct = coc_analysis_json["code_of_conduct"]
        self.contributor_covenant_version = coc_analysis_json["contributor_covenant_version"]
        self.flags = coc_analysis_json.get("flags", [])
        
    def save_to_db(self):
        """
        Saves the current instance of CodeOfConductAnalyzer to the database.
        """
        # Establish a connection to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Ensure the table for the repository exists
        create_table_if_not_exists()

        # Insert the analysis data into the table
        cursor.execute('''
            INSERT INTO coc_analysis (
                repository_name, repository_url, analyzed_at, code_of_conduct, contributor_covenant_version, flags
            ) VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            self.repository_name,
            self.repository_url,
            self.analyzed_at,
            self.code_of_conduct,
            self.contributor_covenant_version,
            json.dumps(self.flags)
        ))

        # Commit the transaction and close the connection
        conn.commit()
        conn.close()

def create_table_if_not_exists():
    """
    Creates a table for the Code of Conduct analysis if it does not already exist.
    """
    # Establish a connection to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coc_analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            repository_name TEXT NOT NULL,
            repository_url TEXT NOT NULL,
            analyzed_at TEXT NOT NULL,
            code_of_conduct TEXT NOT NULL,
            contributor_covenant_version TEXT NOT NULL,
            flags TEXT
        )
    ''')

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
