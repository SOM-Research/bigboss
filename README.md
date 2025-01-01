
# **BigBOSS**

This repository contains the source code for **BigBOSS**, a tool designed to analyze contributions in Open Source Software (OSS) projects. The project currently includes two services:

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

### 4. Verify Configuration
Update `config.py` with the necessary constants and variables, including:

- **MODEL_NAME**: Language model to use.
- **CODE_OF_CONDUCT**: Text of the predefined Code of Conduct.
- **FLAGS**: Predefined categories for behavior analysis.
- **COC_KEYWORDS**: Keywords for detecting Contributor Covenant compliance.

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
    "type": "comment",
    "data": {
        "comment_body": "Thank you for your help!",
        "user": "user123"
    }
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

## **Example Workflow**

1. Send a comment or CoC file for analysis to the `/analyze` endpoint.
2. Retrieve the analysis result, including flags, classifications, and generated responses.
3. Access the saved results in the SQLite database for further processing or auditing.

---

## **Contributing**

We welcome contributions! Please refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for details on our development guidelines.

---

## **Code of Conduct**

This project adheres to a Code of Conduct. By participating, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## **License**

This work is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
