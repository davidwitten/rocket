# Lexer
# Rocket
# Noah Kim

# Import
import fractions
from rocket import errors

# Token List
tokens = [
    "COMMENT", 
    "NUMBER", "VARIABLE",
    
    "QUESTION", "EXCLAMATION",
    "EQUALS", "COLON", "SEMI", "COMMA",

    "ADD", "SUB", "MUL", "DIV", "MOD", "POW",
    "ADDEQ", "SUBEQ", "MULEQ", "DIVEQ", "MODEQ", "POWEQ",
    
    "AT", "DOLLAR",
    
    "EQ", "GT", "LT", "GE", "LE", "NE",

    "ARROW",

    "TILDE",
    
    "NOT", "AND", "OR", "XOR",
    "ANDEQ", "OREQ", "XOREQ",
    
    "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE",
]

# Core structures
def t_COMMENT(t):
    r"\#.*"
    pass

def t_NUMBER(t):
    r"([0-9]*\.[0-9]+|[0-9]+)"
    t.value = fractions.Fraction(t.value)
    return t

t_VARIABLE = r"[a-zA-Z_][a-zA-Z0-9_]*"

# Basic computation
t_EQUALS = r"="
t_ADD = r"\+"
t_SUB = r"-"
t_MUL = r"\*"
t_DIV = r"/"
t_MOD = r"%"
t_POW = r"\*\*"

# Mutating computation
t_ADDEQ = r"\+="
t_SUBEQ = r"-="
t_MULEQ = r"\*="
t_DIVEQ = r"/="
t_MODEQ = r"%="
t_POWEQ = r"\*\*="

# Comparison
t_EQ = "=="
t_GT = r"<"
t_LT = r">"
t_GE = r">="
t_LE = r"<="
t_NE = r"!="

# Logic
t_NOT = r"~"
t_AND = r"&"
t_OR = r"\|"
t_XOR = r"\^"

# Mutating logic
t_ANDEQ = r"&="
t_OREQ = r"\|="
t_XOREQ = r"\^="

# Extended operators
t_QUESTION = r"\?"
t_EXCLAMATION = r"!"
t_ARROW = r"->"
t_DOLLAR = r"\$"
t_AT = r"@"

# Syntax
t_COLON = r":"
t_SEMI = r";"
t_COMMA = r","

# Groups
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

# Whitespace
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

# Errors
def t_error(t):
    print(errors.RocketSyntaxError(t.lexpos, t.lineno, t.value[0]))
    t.lexer.skip(1)

t_ignore = " \t"
