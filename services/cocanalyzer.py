import re
import string
import json
import nltk
from datetime import datetime
from config import COC_KEYWORDS
from database import get_db_connection
from models.cocanalyzer import create_table_if_not_exists
from nltk.corpus import wordnet

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

lemmatizer = nltk.stem.WordNetLemmatizer()

def clean_text(text):
    """
    Cleans the text by removing punctuation, extra spaces, and converting to lowercase.

    :param text: The text to clean.
    :return: The cleaned text.
    """
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

def lemmatize_text(text):
    tokens = nltk.word_tokenize(text)
    lemmatized_text = ' '.join([lemmatizer.lemmatize(token, get_wordnet_pos(token)) for token in tokens])
    return lemmatized_text

def find_flags(text, flags):
    lemmatized_text = lemmatize_text(text)
    results = {}
    for flag, keywords in flags.items():
        for keyword in keywords:
            lemmatized_keyword = lemmatize_text(keyword)
            if re.search(r'\b' + re.escape(lemmatized_keyword) + r'\b', lemmatized_text, re.IGNORECASE):
                if flag not in results:
                    results[flag] = []
                results[flag].append(keyword)
    return results

def detect_contributor_covenant_version(cleaned_text):
    """
    Detects the version of the Contributor Covenant based on key phrases in the cleaned text.

    :param cleaned_text: The cleaned code of conduct text.
    :return: The detected version of the Contributor Covenant.
    """
    phrases_1_4 = [
        "using welcoming and inclusive language",
        "showing empathy towards other community members"
    ]
    
    phrases_2_0 = [
        "accepting responsibility and apologizing to those affected by our mistakes and learning from the experience",
        "trolling insulting or derogatory comments and personal or political attacks"
    ]
    
    if all(phrase in cleaned_text for phrase in phrases_1_4):
        return "1.4"
    
    if all(phrase in cleaned_text for phrase in phrases_2_0):
        return "2.0 or higher"
    
    return "Possibly not based on CC"

def analyze_code_of_conduct(code_of_conduct_text):
    """
    Analyze the provided Code of Conduct text for the presence of specific flags.

    :param code_of_conduct_text: The full Code of Conduct text.
    :return: A JSON object containing the analysis results.
    """
    try:
        # Clean the code of conduct text
        cleaned_text = clean_text(code_of_conduct_text)
        
        # Detect the version of the Contributor Covenant
        version_cc = detect_contributor_covenant_version(cleaned_text)
        
        # Find flags in the cleaned text
        flags = find_flags(cleaned_text, COC_KEYWORDS)
        
        analysis_result = {
            "flags": flags,
            "contributor_covenant_version": version_cc
        }
        
        return analysis_result
    except Exception as e:
        raise

def get_existing_analysis(repository_name, repository_url):
    """
    Get the existing analysis of the Code of Conduct for the given repository.

    :param repository_name: The name of the repository.
    :param repository_url: The URL of the repository.
    :return: A dictionary with the analysis result if already analyzed, otherwise None.
    """
    create_table_if_not_exists()
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT flags, contributor_covenant_version, analyzed_at, code_of_conduct FROM coc_analysis
        WHERE repository_name = ? AND repository_url = ?
    ''', (repository_name, repository_url))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        flags, version, analyzed_at, code_of_conduct = result
        return {
            "status": "already_analyzed",
            "flags": json.loads(flags),
            "contributor_covenant_version": version,
            "analyzed_at": analyzed_at,
            "code_of_conduct": code_of_conduct,
            "repository_name": repository_name,
            "repository_url": repository_url
        }
    
    return None

def process_code_of_conduct(coc_analysis_json):
    """
    Process the Code of Conduct JSON object and return the analysis results.

    :param coc_analysis_json: A JSON object containing the Code of Conduct text and repository details.
    :return: A dictionary containing the analysis results.
    """
    repository_name = coc_analysis_json["repository_name"]
    repository_url = coc_analysis_json["repository_url"]
    code_of_conduct_text = coc_analysis_json["code_of_conduct"]

    # Perform the analysis
    new_analysis_result = analyze_code_of_conduct(code_of_conduct_text)
    new_analysis_result["repository_name"] = repository_name
    new_analysis_result["repository_url"] = repository_url
    new_analysis_result["analyzed_at"] = datetime.utcnow().isoformat()
    new_analysis_result["code_of_conduct"] = code_of_conduct_text
    new_analysis_result["status"] = "analyzed"

    # Check if it has already been analyzed
    existing_analysis_result = get_existing_analysis(repository_name, repository_url)
    if existing_analysis_result:
        # If the analysis results are different, update the status and return the new results
        if existing_analysis_result["flags"] != new_analysis_result["flags"]:
            return new_analysis_result
        
        # If the analysis results are the same, return the existing results with the already_analyzed status
        return existing_analysis_result

    return new_analysis_result
