# Rocket
# David Witten, Noah Kim

# Import
import re
import fractions

# Lexer
tokens = {
    "NUMBER": r"([0-9]*\.[0-9]+|[0-9]+)",
    "PLUS": r"\+",
    "MINUS": r"-",
    "TIMES": r"\*",
    "DIVIDE": r"/",
    "IGNORE": r"\s+",
}

class Token:
    """Token container class."""
    
    def __init__(self, name, value):
        """Initialize a new token."""
        self.name = name
        self.value = value

    def __repr__(self):
        """Representation of a token."""
        return "%s:%s" % (self.name, self.value)

def tokenize(tokens, string):
    """Seperate the string into a list of token objects."""
    tokenized = []
    while string:
        for name, pattern in tokens.items():
            match = re.match("^"+pattern, string)
            if match:
                value = string[match.start():match.end()]
                tokenized.append(Token(name, value))                
                string = string[match.end():]
                break
        else:
            tokenized.append(Token("ERROR", value))
            string = string[1:]
    return tokenized
