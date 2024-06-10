# BigBOSS

This repository contains the source code of the bots develoepd to check ethical issues in OSS projects.

# EthicalAnalyzer Server

## Introduction

EthicalAnalyzer is a server application designed to analyze and respond to comments based on a predefined code of conduct. It leverages a language model to classify comments and generate appropriate responses when necessary.

## Prerequisites

- Python 3.8 or higher
- Flask
- SQLite (or any other database you plan to use)
- An Ollama account to download the language model

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-repository/bigboss.git
cd ethicalanalyzer
```
### 2. Install Dependencies
Make sure you have Python installed. Then, install the required Python packages:

```bash
pip install -r requirements.txt
```
### 3. Download the Language Model
Download the required language model from Ollama:

```bash
ollama download mixtral:8x22b
```

### 4. Configure the Database
Set up your database. By default, SQLite is used. Ensure the get_db_connection function in database.py is correctly configured to connect to your database.

## Project Structure

- `app.py`: Entry point for the Flask application.
- `config.py`: Contains configuration constants.
- `controllers/ethicalanalyzer.py`: Contains the route handler for analyzing comments.
- `models/ethicalanalyzer.py`: Defines the EthicalAnalyzer model and database interaction methods.
- `services/ethicalanalyzer.py`: Handles comment analysis and response generation.
- `routes.py`: Defines the Flask routes.

## Running the Application
Start the Flask server:

```bash
python app.py
```

The server will be accessible at `http://0.0.0.0:5000`.

## API Endpoint

### Analyze Comment

- **URL**: `/analyze`
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Payload**:

```json
{
    "comment_id": "12345",
    "event_type": "issue_comment",
    "user": "user123",
    "user_id": "67890",
    "user_avatar_url": "https://example.com/avatar.jpg",
    "user_html_url": "https://github.com/user123",
    "user_type": "User",
    "comment_body": "Thank you for your help!",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z",
    "event_number": "1",
    "event_title": "Issue title",
    "event_body": "Issue body",
    "event_url": "https://github.com/repo/issues/1",
    "comment_url": "https://github.com/repo/issues/1#issuecomment-1",
    "repository_name": "repo",
    "response_comment": null,
    "response_at": null
}
```
- **Response**:
```json
{
    "comment_id": "12345",
    "event_type": "issue_comment",
    "user": "user123",
    "user_id": "67890",
    "user_avatar_url": "https://example.com/avatar.jpg",
    "user_html_url": "https://github.com/user123",
    "user_type": "User",
    "comment_body": "Thank you for your help!",
    "created_at": "2023-01-01T00:00:00Z",
    "updated_at": "2023-01-01T00:00:00Z",
    "analysis": {
        "classification": "positive",
        "reasons": "Demonstrates empathy and kindness.",
        "flags": ["Empathy and Kindness"],
        "numbered_flags": {"F1": "Empathy and Kindness"}
    },
    "event_number": "1",
    "event_title": "Issue title",
    "event_body": "Issue body",
    "event_url": "https://github.com/repo/issues/1",
    "comment_url": "https://github.com/repo/issues/1#issuecomment-1",
    "repository_name": "repo",
    "response_comment": "@user123 Thank you for your help!",
    "response_at": "2023-01-01T00:00:00Z"
}
```
## Using the Service

To use the EthicalAnalyzer service in your GitHub repository, follow these steps to configure the workflow and connect it to your server.

### 1. Setup Secrets in GitHub

Ensure you have added the following secrets to your GitHub repository:

- `GITHUB_TOKEN`: GitHub token for authentication.
- `SERVER_URL`: URL of your EthicalAnalyzer server.
- `SENDINBLUE_API_KEY`: Sendinblue API key for sending email notifications.
- `EMAIL_FROM`: Sender email address for notifications.
- `EMAIL_TO`: Recipient email address for notifications.
- `BOT_USER`: GitHub username of the bot.
- `BOT_TOKEN`: GitHub token of the bot for performing comment actions.

### 2. Configure GitHub Actions Workflow

Create or update the GitHub Actions workflow file in your repository (e.g., `.github/workflows/check-comments.yml`) with the following configuration:

```yaml
name: Check Comments

on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
  discussion_comment:
    types: [created]

jobs:
  check-comment:
    runs-on: ubuntu-latest
    steps:
      - name: Analyze Comments
        uses: SOM-Research/comment-analyzer@v1.1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          server_url: ${{ secrets.SERVER_URL }}
          sendinblue_api_key: ${{ secrets.SENDINBLUE_API_KEY }}
          email_from: ${{ secrets.EMAIL_FROM }}
          email_to: ${{ secrets.EMAIL_TO }}
          bot_user: ${{ secrets.BOT_USER }}
          bot_token: ${{ secrets.BOT_TOKEN }}
```
# Contributing

This project is part of a research line of the [SOM Research Lab](https://som-research.uoc.edu/), but we are open to contributions from the community. Any comment is more than welcome!

If you are interested in contributing to this project, please read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

# Code of Conduct

At SOM Research Lab we are dedicated to creating and maintaining welcoming, inclusive, safe, and harassment-free development spaces. Anyone participating will be subject to and agrees to sign on to our [Code of Conduct](CODE_OF_CONDUCT.md).

# Governance

The development and community management of this project follows the governance rules described in the [GOVERNANCE.md](GOVERNANCE.md) document.

# License

This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>

The [CC BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) license allows users to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator. The license allows for commercial use. If you remix, adapt, or build upon the material, you must license the modified material under identical terms.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a>
