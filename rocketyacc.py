# Rocket Lex
# Noah Kim

# Import
import fractions
from rocketlex import *

# Namespace
namespace = {}

# Main
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("left", "MODULUS"),
    ("right", "NEGATE"),
    ("left", "POWER"),
)

def p_statement_assignment(p):
    """statement : assignment"""
    pass

def p_assignment(p):
    """assignment : VARIABLE COLON expression SEMI"""
    namespace[p[1]] = p[3]

def p_statement_expression(p):
    """statement : expression"""
    p[0] = p[1]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_parenthesis(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_unary(p):
    """expression : MINUS expression %prec NEGATE"""
    if p[1] == "-": p[0] = -p[2]

def p_expression_binary(p):
    """expression : expression POWER expression
                  | expression MODULUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression PLUS expression
                  | expression MINUS expression
    """
    if p[2] == "^": p[0] = p[1] ** p[3]
    elif p[2] == "%": p[0] = p[1] % p[3]
    elif p[2] == "*": p[0] = p[1] * p[3]
    elif p[2] == "/": p[0] = p[1] / p[3]
    elif p[2] == "+": p[0] = p[1] + p[3]
    elif p[2] == "-": p[0] = p[1] - p[3]

def p_error(p):
    print("error", p)
