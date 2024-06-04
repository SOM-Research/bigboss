import json
from datetime import datetime
from config import CODE_OF_CONDUCT, FLAGS, MODEL_NAME, ANALYZE_PROMPT_TEMPLATE, RESPONSE_PROMPT_TEMPLATE, EXPLANATION, REQUIRED_FLAGS
from models.ethicanalyzer import EthicalAnalyzer
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Initialize the language model (LLM) with the specified model name
llm = Ollama(model=MODEL_NAME)

# Initialize the output parser
output_parser = StrOutputParser()

# Define the prompt templates
analyze_prompt = ChatPromptTemplate.from_messages(ANALYZE_PROMPT_TEMPLATE)
response_prompt = ChatPromptTemplate.from_messages(RESPONSE_PROMPT_TEMPLATE)

# Create the processing chain by combining the prompt, model, and output parser
chain = analyze_prompt | llm | output_parser
response_chain = response_prompt | llm | output_parser

def process_comment(comment_to_analyze):
    """
    Analyzes a given comment using the language model and returns the analysis result.

    :param comment_to_analyze: The comment text to be analyzed.
    :return: The response from the language model as a JSON string.
    """
    return chain.invoke({"input": CODE_OF_CONDUCT + comment_to_analyze})

def generate_response(comment_to_respond):
    """
    Generates a response to a given comment using the language model.

    :param comment_to_analyze: The comment text to generate a response for.
    :return: The generated response from the language model as a JSON string.
    """
    return response_chain.invoke({"input": EXPLANATION + comment_to_respond})

def analyze_and_respond(comment_json):
    """
    Analyzes a comment JSON object, generates a response if certain flags are present, and returns the modified comment JSON.

    :param comment_json: A dictionary containing the comment data.
    :return: The modified comment JSON with the analysis and possibly a generated response.
    """
    try:
        # Extract the comment body from the JSON object
        comment_to_analyze = comment_json["comment_body"]
        user = comment_json["user"]

        # Analyze the comment using the language model
        result = process_comment(comment_to_analyze)
        
        # Ensure the result is a valid JSON string
        if not result:
            raise ValueError("Received an empty response from the language model")

        result_dict = json.loads(result)

        # Generate the list of numbered flags based on the analysis
        flags = result_dict.get("flags", [])
        numbered_flags = {FLAGS[flag]: flag for flag in flags if flag in FLAGS}
        result_dict["numbered_flags"] = numbered_flags

        # Add the analysis results to the original JSON
        comment_json["analysis"] = result_dict
        
        if any(flag in flags for flag in REQUIRED_FLAGS):
            generated_response = generate_response(comment_to_analyze)
            if generated_response:
                response_with_user = f"@{user} {generated_response}"
                comment_json["response_comment"] = response_with_user
                comment_json["response_at"] = datetime.utcnow().isoformat()

        # Create an EthicalAnalyzer object with the processed comment data
        ethicanal = EthicalAnalyzer(comment_json)
        return ethicanal
    except Exception as e:
        raise
