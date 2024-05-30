import json
from config import CODE_OF_CONDUCT, FLAGS, MODEL_NAME, PROMPT_TEMPLATE
from models.ethicanal_model import EthicAnal
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# Initialize the language model (LLM) with the specified model name
llm = Ollama(model=MODEL_NAME)
# Initialize the output parser
output_parser = StrOutputParser()
# Define the prompt template using messages from the configuration
prompt = ChatPromptTemplate.from_messages(PROMPT_TEMPLATE)

# Create the processing chain by combining the prompt, model, and output parser
chain = prompt | llm | output_parser

def process_comment(comment_to_analyze):
    """
    Analyzes a given comment using the language model and returns the analysis result.

    :param comment_to_analyze: The comment text to be analyzed.
    :return: The response from the language model as a JSON string.
    """
    response = chain.invoke({"input": CODE_OF_CONDUCT + comment_to_analyze})
    return response

def analyze_comment(comment_json):
    """
    Processes a comment JSON object, analyzes it, and returns an EthicAnal object.

    :param comment_json: A dictionary containing the comment data.
    :return: An EthicAnal object with the analyzed data.
    """
    # Extract the comment body from the JSON object
    comment_to_analyze = comment_json["comment_body"]

    # Analyze the comment using the language model
    result = process_comment(comment_to_analyze)
    result_dict = json.loads(result)

    # Generate the list of numbered flags based on the analysis
    flags = result_dict.get("flags", [])
    numbered_flags = {FLAGS[flag]: flag for flag in flags if flag in FLAGS}
    result_dict["numbered_flags"] = numbered_flags

    # Add the analysis results to the original JSON
    comment_json["analysis"] = result_dict

    # Create an EthicAnal object with the processed comment data
    ethicanal = EthicAnal(comment_json)
    return ethicanal
