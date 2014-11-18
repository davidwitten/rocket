# Rocket
# David Witten, Noah Kim

# Import
import fractions
from ply import lex
from ply import yacc

# Lex
tokens = (
    "NAME",

    "NUMBER", "STRING",

    "EQUALS",
    "PLUS", "MINUS", "TIMES", "DIVIDE", "MOD", "POWER",
    "OR", "AND", "NOT",
    "LT", "LE", "GT", "GE", "EQ", "NE",

    "LPAREN", "RPAREN",
    "LBRACKET", "RBRACKET",
    "COMMA", "PERIOD",
    "SEMI", "COLON",
)

t_NAME = r"[a-zA-Z_][0-9a-zA-Z_]*"

def t_NUMBER(t):
    r"\d+(\.\d+)?"
    t.value = fractions.Fraction(t.value)
    return t

t_STRING = r'"[^"\\\n]*(\\.[^"\\\n]*)*"'
    
t_EQUALS = r"="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MOD = r"%"
t_POWER = r"\^"
t_OR = r"or"
t_AND = r"and"
t_NOT = r"not"
t_LT = r"<"
t_LE = r"<="
t_GT = r">"
t_GE = r">="
t_EQ = r"=="
t_EQ = r"<>"

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_COMMA = r","
t_PERIOD = r"\."
t_SEMI = r";"
t_COLON = r":"

def t_NEWLINE(self, t):
        r"\n+"
        t.lexer.lineno += t.value.count("\n")

t_ignore = " \t"

def t_error(t):
    print("unknown character: %s" % t.value)

lex.lex()
