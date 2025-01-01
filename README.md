
# **BigBOSS**

This repository contains the source code for **BigBOSS**, a tool designed to monitor and analyze contributions and **Codes of Conduct (CoC)** in Open Source Software (OSS) projects. The project includes two main services:

- **`conductAnalyzer`**: Analyzes comments for adherence to a predefined code of conduct and generates appropriate responses.
- **`cocAnalyzer`**: Processes and evaluates code of conduct (CoC) files, identifies ethical patterns, and detects compliance with Contributor Covenant guidelines.

---

## **Overview**

This project provides:

- Scripts for:
  - Detecting and analyzing **comments** for appropriate behavior (**conductAnalyzer**).
  - Detecting and analyzing **Code of Conduct (CoC)** content (**cocAnalyzer**).
  - Evaluating alignment with **Contributor Covenant** guidelines.
  - Extracting ethical flags from comments and CoC files based on predefined patterns.

---

## **Requirements**

- Python 3.8 or higher
- Flask
- SQLite (or an alternative database engine)
- Ollama for downloading and using the language model

To install dependencies, run:

```bash
pip install -r requirements.txt
```

---

## **Setup**

### 1. Clone the Repository
```bash
git clone https://github.com/your-repository/bigboss.git
cd bigboss
```

### 2. Configure Database
By default, the tool uses SQLite. Ensure the database connection in `database.py` is configured according to your needs.

### 3. Download the Language Model
Download the required model using Ollama:

```bash
ollama download mixtral:8x22b
```
--- 

## **GitHub Actions Integration**

BigBOSS relies on a set of **GitHub Actions** to enable seamless monitoring and analysis of contributions and Codes of Conduct in OSS repositories. These actions automate workflows for analyzing comments, managing Code of Conduct files, and creating issues or pull requests as needed.

### **Required Actions**

To ensure full functionality, the following GitHub Actions must be configured in your repository:

1. **`Comment Analyzer`**: Handles analysis of comments in issues, pull requests, and discussions, and triggers appropriate actions such as generating responses or notifying repository owners.

2. **`Code of Conduct Analyzer`**: Processes and sends Code of Conduct files to the analysis server for evaluation.

3. **`Code of Conduct Initializer`**: Adds or updates the `CODE_OF_CONDUCT.md` file in repositories where it is missing or outdated.

4. **`Issue Manager`**: Creates issues for repositories with incomplete or missing Code of Conduct guidelines.


### **Setup Instructions for Actions**

Ensure the following steps are completed to integrate the actions:
- Add the **required secrets** (e.g., `GITHUB_TOKEN`, `SERVER_URL`, `BOT_USER`, `BOT_TOKEN`) to your GitHub repository.
- Include the appropriate workflow files (e.g., `.github/workflows/comment-analyzer.yml`) in your repository.
- Configure the actions with the necessary inputs to match your project's requirements.

### **Benefits of Integration**

By utilizing GitHub Actions, BigBOSS provides:
- Real-time analysis of contributions and Code of Conduct files.
- Automated feedback and moderation for comments.
- Streamlined updates to Code of Conduct files and documentation.

---

## **Running the Application**

Start the Flask server:

```bash
python app.py
```

The server will be accessible at: `http://0.0.0.0:5000`.

---

## **Services and Endpoints**

### 1. **`conductAnalyzer`**

Analyzes comments for ethical and professional behavior. Generates responses for flagged comments.

**Endpoint**: `/analyze`  
**Method**: `POST`  
**Payload** (example):
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

### 2. **`cocAnalyzer`**

Processes and evaluates Code of Conduct (CoC) files for compliance and ethical patterns.

**Endpoint**: `/analyze`  
**Method**: `POST`  
**Payload** (example):
```json
{
    "type": "code_of_conduct",
    "repository_name": "repo",
    "repository_url": "https://github.com/repo",
    "code_of_conduct": "This is the text of the CoC file."
}
```

---

## **Project Structure**

- **`app.py`**: Entry point for the Flask application.
- **`config.py`**: Contains constants and configurations for both services.
- **`controllers/`**:
  - **`controller.py`**: Defines the route handler for comment and CoC analysis.
- **`models/`**:
  - **`conductanalyzer.py`**: Defines data handling and database interactions for comment analysis.
  - **`cocanalyzer.py`**: Defines data handling and database interactions for CoC analysis.
- **`services/`**:
  - **`conductanalyzer.py`**: Implements comment analysis using a language model.
  - **`cocanalyzer.py`**: Implements CoC evaluation and flag detection.

---


## **Contributing**

We welcome contributions! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our development guidelines.

---

## **Code of Conduct**

This project adheres to a Code of Conduct. By participating, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## **License**

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
