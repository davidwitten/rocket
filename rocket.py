# Rocket
# David Witten, Noah Kim

# Import
import fractions
from ply import lex
from ply import yacc

#from rocketlex import *
from rocketyacc import *

# Setup
namespace = {}

# Lex
tokens = ["PLUS", "MINUS", "TIMES", "DIVIDE", "LPAREN", "RPAREN", "COLON",
          "VARIABLE", "NUMBER"]

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"

t_LPAREN = r"\("
t_RPAREN = r"\)"

t_COLON = r":"
t_VARIABLE = r"[a-zA-Z]"

def t_NUMBER(t):
    r"([0-9]*\.[0-9]+|[0-9]+)"
    t.value = fractions.Fraction(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("invalid character %s" % t.value)
    t.lexer.skip(1)

t_ignore = " \t"

lex.lex()
s = "1+5*3"
lex.input(s)

# Yacc
yacc.yacc()


