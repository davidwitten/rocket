# Lexer
# Rocket
# Noah Kim

# Import
import fractions

# Tweaks
def __nice__(fraction):
    """Get the aesthetically nice value of a fraction."""
    value = fraction._numerator / fraction._denominator
    return str(int(value) if int(value) == value else value)
fractions.Fraction.__repr__ = __nice__
fractions.Fraction.__str__ = __nice__

# Errors
INVALID_CHAR = "Lexer Error: Invalid character '%s' at index %i"

# Token List
tokens = [
    "COMMENT", 
    "NUMBER", "VARIABLE",
    "QUESTION", "EXCLAMATION",
    "COLON", "SEMI", "COMMA",
    "PLUS", "MINUS", "TIMES", "DIVIDE", "MODULUS", "POWER", "AT", "DOLLAR",
    "EQUALS", "GREATER", "LESS", "AND", "OR", "NOT",
    "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE",
]

# Token Definitions
def t_COMMENT(t):
    r"\#.*"
    pass

def t_NUMBER(t):
    r"([0-9]*\.[0-9]+|[0-9]+)"
    t.value = fractions.Fraction(t.value)
    return t

t_VARIABLE = r"[a-zA-Z_][a-zA-Z0-9_]*"

t_COLON = r":"
t_SEMI = r";"
t_COMMA = r","
t_QUESTION = r"\?"
t_EXCLAMATION = r"!"

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULUS = r"%"
t_POWER = r"\^"

t_AT = r"@"
t_DOLLAR = r"\$"

t_EQUALS = r"="
t_GREATER = r"<"
t_LESS = r">"
t_AND = r"&"
t_OR = r"\|"
t_NOT = r"~"

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(INVALID_CHAR % (t.value, t.lexpos))
    t.lexer.skip(1)

t_ignore = " \t"
