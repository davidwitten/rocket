# Rocket Lex
# Noah Kim

# Import
import fractions
from ply import lex

# Main
tokens = [
    "COMMENT", "NUMBER", "VARIABLE",
    
    "BACKSLASH", "QUESTION", "EXCLAMATION",
    "COLON", "SEMI", "PERIOD", "COMMA",

    "PLUS", "MINUS", "TIMES", "DIVIDE", "MOD", "POWER", "DOLLAR",
    "EQUALS", "GREATER", "LESS", "AND", "OR", "NOT",

    "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE",
]

def t_COMMENT(t):
    r"\#.*"
    pass

def t_NUMBER(t):
    r"([0-9]*\.[0-9]+|[0-9]+)"
    t.value = fractions.Fraction(t.value)
    return t

t_VARIABLE = r"[a-zA-Z]"

t_BACKSLASH = r"\\"
t_QUESTION = r"\?"
t_EXCLAMATION = r"!"
t_COLON = r":"
t_SEMI = r";"
t_PERIOD = "."
t_COMMA = r","

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MOD = r"%"
t_POWER = r"\^"
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
    print("invalid character %s" % t.value)
    t.lexer.skip(1)

t_ignore = " \t"
