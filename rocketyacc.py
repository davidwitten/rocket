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

def p_uminus(p):
    """expression : MINUS expression %prec UMINUS"""
    p[0] = -p[2]

def p_expression(p):
    """expression : NUMBER
                  | LPAREN expression RPAREN
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
    """
    if len(p) == 2: p[0] = p[1]
    elif p[1] == "(": p[0] = p[2]
    elif p[2] == "+": p[0] = p[1] + p[3]
    elif p[2] == "-": p[0] = p[1] - p[3]
    elif p[2] == "*": p[0] = p[1] * p[3]
    elif p[2] == "/": p[0] = p[1] / p[3]

def p_error(p):
    print("error", p)
