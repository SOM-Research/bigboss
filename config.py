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

COC_KEYWORDS = {
    "F1": [
        "being kind",
        "empathy",
        "empathic",
        "kindness",
    ],

    "F2": [
        "respect in your speech"
        "show respect",
        "with respect",
        "respect towards others",
        "be respectful",
        "respect for differences",
        "different viewpoints",
        "differing viewpoints",
        "differing opinions",
        "diverse perspectives",
        "open to different possibilities",
        "eliminate biases",
        "accommodate differences",

    ],
    "F3": [
        "constructive feedback",
        "constructive criticism",
        "respectful criticism",
        "tactful feedback",
        "gracefully accepting",
        "receptive to comments",
        "constructively resolve conflict",
        "feedback for improvement",
        "thoughtful addressing"
    ],
    "F4": [
        "responsibility and apologizing",
        "apologize",
        "take responsibility",
        "acknowledge mistakes",
        "admit fault",
    ],
    "F5": [
        "be collaborative",
        "best for the community",
        "overall community",
        "common good",
        "community benefit",
        "collective interest",
        "broader community",
        "community focus",
    ],
    "F6": [
        "sexist",
        "sexualized comments",
        "sexual language",
        "sexualized language",
        "sexual imagery",
        "inappropriate sexual content",
        "sexually explicit",
        "unwelcome sexual attention",
        "sexually suggestive",
        "groping",
        "sexual advances",
        "sexual jokes",
        "sexual comments"
    ],
    "F7": [
        "trolling", 
        "insulting",
        "derogatory comments",
        "derogatory remarks",
        "demeaning language",
        "insults",
        "personal attacks",
        "ridicule",
        "offensive jokes",
    ],
    "F8": [
        "harass",
        "harassing",
        "harassment",
        "stalking",
        "intimidation",
        "bullying",
        "threatened",
        "threats",
        "persistent unwanted contact",
    ],
    "F9": [
        "private information",
        "publishing private information",
        "doxxing",
        "doxing",
        "sharing personal data",
        "leaking private info",
        "exposing private details",
        "unconsented disclosure",
        "confidential information",
        "privacy breach",
        "revealing personal information",
        "unauthorized sharing"
    ],
    "F10": [
        "considered inappropriate",
        "professional setting",
        "behaving professionally",
        "inappropriate conduct",
        "unprofessional behavior",
        "professional audience",
        "inappropriate actions",
        "unsuitable behavior",
        "unacceptable conduct",
        "improper behavior",
        "inappropriate language"
    ],
}