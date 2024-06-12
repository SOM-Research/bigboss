import re
import json
from datetime import datetime
from config import MODEL_NAME, EXPLANATION_COCANALYZER, FLAGS_COCANALYZER, COCANALYZER_PROMPT_TEMPLATE
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm = Ollama(model=MODEL_NAME)
output_parser = StrOutputParser()
cocanalyzer_prompt = ChatPromptTemplate.from_messages(COCANALYZER_PROMPT_TEMPLATE)
chain = cocanalyzer_prompt | llm | output_parser

def extract_standards(text):
    """
    Extract the "Our Standards" section from the Code of Conduct text.

    :param text: The full Code of Conduct text.
    :return: The extracted "Our Standards" section.
    """
    pattern = re.compile(r"(## Our Standards)(.*?)(## [A-Za-z ]+|$)", re.DOTALL)
    match = pattern.search(text)
    if match:
        return match.group(2).strip()
    else:
        raise ValueError("Section 'Our Standards' not found.")

def analyze_code_of_conduct(code_of_conduct_text):
    """
    Analyze the provided Code of Conduct text for the presence of specific flags.

    :param code_of_conduct_text: The full Code of Conduct text.
    :return: A JSON object containing the analysis results.
    """
    try:
        standards_section = extract_standards(code_of_conduct_text)
        
        input_text = f"{EXPLANATION_COCANALYZER}\n\n{FLAGS_COCANALYZER}\n\n{standards_section}"
        
        response = chain.invoke({"input": input_text})
        
        if not response:
            raise ValueError("Received an empty response from the language model")
        
        response_json = json.loads(response)
        return response_json
    except Exception as e:
        raise

def process_code_of_conduct(coc_analysis_json):
    """
    Process the Code of Conduct JSON object and return the analysis results.

    :param coc_analysis_json: A JSON object containing the Code of Conduct text and repository details.
    :return: A dictionary containing the analysis results.
    """
    code_of_conduct_text = coc_analysis_json["code_of_conduct"]
    repository_name = coc_analysis_json["repository_name"]
    repository_url = coc_analysis_json["repository_url"]

    analysis_result = analyze_code_of_conduct(code_of_conduct_text)
    analysis_result["repository_name"] = repository_name
    analysis_result["repository_url"] = repository_url
    analysis_result["analyzed_at"] = datetime.utcnow().isoformat()
    analysis_result["code_of_conduct"] = code_of_conduct_text
    return analysis_result
