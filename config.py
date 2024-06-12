MODEL_NAME = "mixtral:8x22b"

# ETHICALANALYZER

CODE_OF_CONDUCT = """
The Code of Conduct is based on the following guidelines:

**Positive Flags:**
1. Empathy and Kindness: Demonstrating understanding and compassion towards others.
2. Respect for Differences: Valuing diverse perspectives and backgrounds.
3. Constructive Feedback: Providing feedback that is helpful and aimed at improvement.
4. Responsibility and Apology: Taking responsibility for one's actions and apologizing when necessary.
5. Common Good: Acting in ways that benefit the broader community.
6. Inclusive language: Using inclusive language.

**Negative Flags:**
1. Sexualized Language or Imagery: Using language or imagery that is inappropriate and sexual in nature.
2. Insulting or Derogatory Comments: Making comments that insult or demean others.
3. Public or Private Harassment: Engaging in behavior that intimidates or harasses others.
4. Publishing Private Information: Sharing private information about others without consent.
5. Inappropriate Conduct: Behaving in a manner that is not suitable for the setting.
6. Hate Speech: Using language that promotes hatred against individuals or groups.

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
  "reasons": "Demonstrates empathy and kindness.",
  "flags": ["Empathy and Kindness"]
}

**Comment 2:**
"You are incompetent! You don't know what you're doing."

**JSON:**
{
  "comment": "You are incompetent! You don't know what you're doing.",
  "classification": "negative",
  "reasons": "Insulting and derogatory comments.",
  "flags": ["Insulting or Derogatory Comments"]
}

**Comment 3:**
"We don't want people like you here. Go back to where you belong."

**JSON:**
{
  "comment": "We don't want people like you here. Go back to where you belong.",
  "classification": "negative",
  "reasons": "Use of hate speech.",
  "flags": ["Hate Speech"]
}

**Comment:**
"""

EXPLANATION_ETHICALANALYZER = """
This response was generated to thank a user who left a comment on a GitHub issue.
A suitable and kind response is provided.
The responses should be in english and one sentence.
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
    "Empathy and Kindness": "F1",
    "Respect for Differences": "F2",
    "Constructive Feedback": "F3",
    "Responsibility and Apology": "F4",
    "Common Good": "F5",
    "Sexualized Language or Imagery": "F6",
    "Insulting or Derogatory Comments": "F7",
    "Public or Private Harassment": "F8",
    "Publishing Private Information": "F9",
    "Inappropriate Conduct": "F10",
    "Hate Speech": "F11"
}

REQUIRED_FLAGS = {"Empathy and Kindness", "Respect for Differences", "Constructive Feedback", "Responsibility and Apology", "Common Good"}


# COCANALYZER

COCANALYZER_PROMPT_TEMPLATE = [
    ("system", "You are an ethical analyzer for GitHub repositories. Analyze the following Code of Conduct for the presence of specific flags."),
    ("user", "{input}")
]

EXPLANATION_COCANALYZER = """
Analyze the provided Code of Conduct text for the presence of the following flags (Positive and Negative). Respond in a structured JSON format listing any flags found.

Example Output:
{
  "positive_flags": [
    "F1: Empathy and Kindness",
    "F2: Respect for Differences"
  ],
  "negative_flags": [
    "F6: Sexualized Language or Imagery"
  ]
}

Example Output:
{
  "positive_flags": [
    "F3: Constructive Feedback",
    "F4: Responsibility and Apology"
  ],
  "negative_flags": [
    "F7: Insulting or Derogatory Comments"
  ]
}

Example Output:
{
  "positive_flags": [
    "F5: Common Good"
  ],
  "negative_flags": [
    "F8: Public or Private Harassment",
    "F9: Publishing Private Information"
  ]
}
"""

FLAGS_COCANALYZER = """
**FLAGS**:
**Positive Flags:**
F1: Empathy and Kindness: Demonstrating understanding and compassion towards others.
F2: Respect for Differences: Valuing diverse perspectives and backgrounds.
F3: Constructive Feedback: Providing feedback that is helpful and aimed at improvement.
F4: Responsibility and Apology: Taking responsibility for one's actions and apologizing when necessary.
F5: Common Good: Acting in ways that benefit the broader community.
F6. Inclusive language: Using inclusive language.

**Negative Flags:**
F7: Sexualized Language or Imagery: Using language or imagery that is inappropriate and sexual in nature.
F8: Insulting or Derogatory Comments: Making comments that insult or demean others.
F9: Public or Private Harassment: Engaging in behavior that intimidates or harasses others.
F10: Publishing Private Information: Sharing private information about others without consent.
F11: Inappropriate Conduct: Behaving in a manner that is not suitable for the setting.
F12: Hate Speech: Using language that promotes hatred against individuals or groups.

**CODE_OF_CONDUCT:**
"""