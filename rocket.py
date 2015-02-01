# Rocket
# David Witten, Noah Kim

# Import
import fractions
from ply import lex
from ply import yacc

# Setup
namespace = {}

# Lexer
tokens = ["COMMENT", "NUMBER", "NVAR", "LVAR"]
literals = [
    "\\",
    ":",
    "+", "-", "*", "/", "%", "^", "$",
    "=", ">", "<", "&", "|", "~",
    "?", "!",
    ",", ".", ";"
]

def t_COMMENT(t):
    r"\#.*"
    pass

def t_NUMBER(t):
    r"\d+(\.d+)?"
    t.value = fractions.Fraction(t.value)
    return t

t_NVAR = r"[a-z]"
t_LVAR = r"[A-Z]"

t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_LBRACE = r"\{"
t_RBRACE = r"\}"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = " \t"

def t_error(t):
    print("bad character %s" % t.value)
    t.lexer.skip(1)

lex.lex()
#s = "a:1;?(a>0){a:a+1;}{\\a;}"
#lex.input(s)




