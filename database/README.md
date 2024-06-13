# Database Setup

This project requires a SQLite database that is not included in the repository for security reasons. Follow these steps to set up the database locally.

## Steps to Set Up the Database

1. **Create the Database Directory:**

   Make sure the `database` directory exists in the root of the project.

   ```bash
   mkdir -p database

2. **Create the Database File:**

   Use the following Python script to create the database file and the necessary tables. Save this script as `create_db.py` in the root of your project.

   ```python
   import sqlite3

   # Connect to the database (this will create it if it doesn't exist)
   conn = sqlite3.connect('database/conductbot.db')

   # Create a cursor
   cursor = conn.cursor()

   # Create the table
   cursor.execute('''
   CREATE TABLE IF NOT EXISTS comments (
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
       response_comment TEXT,
       issue_number TEXT,
       issue_title TEXT,
       issue_body TEXT,
       issue_url TEXT,
       comment_url TEXT,
       repository_name TEXT NOT NULL,
       repository_full_name TEXT,
       repository_html_url TEXT
   )
   ''')

   # Commit the changes and close the connection
   conn.commit()
   conn.close()

   print("Database and table created successfully.")


3. **Run the Script:**

    Execute the script to create the database file.

    ```bash
    python create_db.py
