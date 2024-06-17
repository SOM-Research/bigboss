MODEL_NAME = "mixtral:8x22b"

# conductANALYZER

CODE_OF_CONDUCT = """
The Code of Conduct is based on the following guidelines:

**Positive Flags:**
1. Demonstrating empathy and kindness toward other people
2. Being respectful of differing opinions, viewpoints, and experiences
3. Giving and gracefully accepting constructive feedback
4. Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience
5. Focusing on what is best not just for us as individuals, but for the overall community

**Negative Flags:**
1. The use of sexualized language or imagery, and sexual attention or advances of any kind
2. Trolling, insulting or derogatory comments, and personal or political attacks
3. Public or private harassment
4. Publishing others’ private information, such as a physical or email address, without their explicit permission
5. Other conduct which could reasonably be considered inappropriate in a professional setting

**Neutral Flags**
A comment is considered neutral when it does not fall under any of the described flags.

Negative comments can't have positive flags.
Here are some examples of comments and the expected JSON output:

**Comment 1:**
"Thank you for your help, I really appreciate your time and effort."

**JSON:**
{
  "comment": "Thank you for your help, I really appreciate your time and effort.",
  "classification": "positive",
  "reasons": "Demonstrating empathy and kindness toward other people.",
  "flags": ["Demonstrating empathy and kindness toward other people"]
}

**Comment 2:**
"You are incompetent! You don't know what you're doing."

**JSON:**
{
  "comment": "You are incompetent! You don't know what you're doing.",
  "classification": "negative",
  "reasons": "Trolling, insulting or derogatory comments, and personal or political attacks.",
  "flags": ["Trolling, insulting or derogatory comments, and personal or political attacks"]
}

**Comment 3:**
"We don't want people like you here. Go back to where you belong."

**JSON:**
{
  "comment": "We don't want people like you here. Go back to where you belong.",
  "classification": "negative",
  "reasons": "Other conduct which could reasonably be considered inappropriate in a professional setting.",
  "flags": ["Other conduct which could reasonably be considered inappropriate in a professional setting"]
}

**Comment:**
"""

EXPLANATION_CONDUCTANALYZER = """
This response was generated to thank a user who left a comment on a GitHub issue.
A suitable and kind response is provided.
The responses should be in English and one sentence.
"""

ANALYZE_PROMPT_TEMPLATE = [
    ("system", "Your task is to analyze community comments and generate a JSON output that includes the comment, a classification (positive or negative), the reasons for the classification, and a list of relevant flags based on the given Code of Conduct."),
    ("user", "{input}")
]

RESPONSE_PROMPT_TEMPLATE = [
    ("system", "You are a contributor to the repository. Generate a kind and grateful response to the following positive comment received on GitHub. Respond in English."),
    ("user", "{input}")
]

FLAGS = {
    "Demonstrating empathy and kindness toward other people": "F1",
    "Being respectful of differing opinions, viewpoints, and experiences": "F2",
    "Giving and gracefully accepting constructive feedback": "F3",
    "Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience": "F4",
    "Focusing on what is best not just for us as individuals, but for the overall community": "F5",
    "The use of sexualized language or imagery, and sexual attention or advances of any kind": "F6",
    "Trolling, insulting or derogatory comments, and personal or political attacks": "F7",
    "Public or private harassment": "F8",
    "Publishing others’ private information, such as a physical or email address, without their explicit permission": "F9",
    "Other conduct which could reasonably be considered inappropriate in a professional setting": "F10"
}

REQUIRED_FLAGS = {"Demonstrating empathy and kindness toward other people", "Being respectful of differing opinions, viewpoints, and experiences", "Giving and gracefully accepting constructive feedback", "Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience", "Focusing on what is best not just for us as individuals, but for the overall community"}


# COCANALYZER

COCANALYZER_PROMPT_TEMPLATE = [
    ("system", "You are a conduct analyzer for GitHub repositories. Analyze the following Code of Conduct for the presence of specific flags."),
    ("user", "{input}")
]

EXPLANATION_COCANALYZER = """
Analyze the provided Code of Conduct text for the presence of the following flags (Positive and Negative). Respond in a structured JSON format listing any flags found.

Example Output:
{
  "positive_flags": [
    "F1: Demonstrating empathy and kindness toward other people",
    "F2: Being respectful of differing opinions, viewpoints, and experiences"
  ],
  "negative_flags": [
    "F6: The use of sexualized language or imagery, and sexual attention or advances of any kind"
  ]
}

Example Output:
{
  "positive_flags": [
    "F3: Giving and gracefully accepting constructive feedback",
    "F4: Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience"
  ],
  "negative_flags": [
    "F7: Trolling, insulting or derogatory comments, and personal or political attacks"
  ]
}

Example Output:
{
  "positive_flags": [
    "F5: Focusing on what is best not just for us as individuals, but for the overall community"
  ],
  "negative_flags": [
    "F8: Public or private harassment",
    "F9: Publishing others’ private information, such as a physical or email address, without their explicit permission"
  ]
}
"""

FLAGS_COCANALYZER = """
**FLAGS**:
**Positive Flags:**
F1: Demonstrating empathy and kindness toward other people
F2: Being respectful of differing opinions, viewpoints, and experiences
F3: Giving and gracefully accepting constructive feedback
F4: Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience
F5: Focusing on what is best not just for us as individuals, but for the overall community

**Negative Flags:**
F6: The use of sexualized language or imagery, and sexual attention or advances of any kind
F7: Trolling, insulting or derogatory comments, and personal or political attacks
F8: Public or private harassment
F9: Publishing others’ private information, such as a physical or email address, without their explicit permission
F10: Other conduct which could reasonably be considered inappropriate in a professional setting

**CODE_OF_CONDUCT:**
"""