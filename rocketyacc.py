# Rocket Lex
# Noah Kim

# Import
import fractions
from ply import yacc

# Main
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("left", "POWER"),
    ("right", "UMINUS"),
)

def p_expression(p):
    """expression : NUMBER
                  | MINUS NUMBER %prec UMINUS
                  | LPAREN expression RPAREN
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
    """
    if len(p) == 2: p[0] = p[1]
    elif len(p) == 3: p[0] = -p[2]
    elif p[1] == "(": p[0] = p[2]
    elif p[2] == "+": p[0] = p[1] + p[3]
    elif p[2] == "-": p[0] = p[1] - p[3]
    elif p[2] == "*": p[0] = p[1] * p[3]
    elif p[2] == "/": p[0] = p[1] / p[3]

def p_empty(p):
    print("empty")

def p_error(p):
    print("error", p)
