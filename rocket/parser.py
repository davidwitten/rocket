# Parser
# Rocket
# Noah Kim

# Import
import fractions
from rocket.lexer import tokens

# Namespace
namespace = {}

# Precedence
precedence = (
    ("right", "OR"),
    ("right", "AND"),
    ("right", "EQUALS"),
    ("right", "GREATER", "LESS"),
    ("left", "ADD", "SUBTRACT"),
    ("left", "MULTIPLY", "DIVIDE"),
    ("left", "MODULUS"),
    ("left", "AT"),
    ("right", "NEGATE", "NOT", "DOLLAR"),
    ("left", "POWER"),
)

# Parsing Definitions
def p_statements(p):
    """statements : statements statement SEMI
                  | statement SEMI
                  | SEMI
    """
    if len(p) == 4: p[0] = p[1] + [p[2]]
    elif len(p) == 3: p[0] = [p[1]]

def p_statement_assignment(p):
    """statement : assignment"""
    p[0] = p[1]

def p_assignment(p):
    """assignment : VARIABLE COLON expression"""
    p[0] = ("set", p[1], p[3])

def p_statement_expression(p):
    """statement : expression"""
    p[0] = ("out", p[1])

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_list(p):
    """expression : LBRACKET list RBRACKET
                  | LBRACKET RBRACKET"""
    if len(p) == 4: p[0] = p[2]  # NO AST FOR PARSED LITERAL
    elif len(p) == 3: p[0] = []
    
def p_list(p):
    """list : list COMMA expression
            | expression"""
    if len(p) == 2: p[0] = [p[1]]  # NO AST FOR PARSED LITERAL
    else: p[0] = p[1] + [p[3]]

def p_expression_variable(p):
    """expression : VARIABLE"""
    p[0] = ("get", p[1])

def p_expression_index(p):
    """expression : expression AT expression"""
    p[0] = ("index", p[0], p[1])

def p_expression_parenthesis(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_length(p):
    """expression : DOLLAR expression"""
    p[0] = ("len", p[2])

def p_expression_math(p):
    """expression : SUBTRACT expression %prec NEGATE
                  | expression POWER expression
                  | expression MODULUS expression
                  | expression MULTIPLY expression
                  | expression DIVIDE expression
                  | expression ADD expression
                  | expression SUBTRACT expression"""
    
    if p[1] == "-": p[0] = ("negate", p[2])
    elif p[2] == "^": p[0] = ("power", p[1], p[3])
    elif p[2] == "%": p[0] = ("modulus", p[1], p[3])
    elif p[2] == "*": p[0] = ("multiply", p[1], p[3])
    elif p[2] == "/": p[0] = ("divide", p[1], p[3])
    elif p[2] == "+": p[0] = ("add", p[1], p[3])
    elif p[2] == "-": p[0] = ("subtract", p[1], p[3])

def p_expression_comparison(p):
    """expression : NOT expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression EQUALS expression
                  | expression AND expression
                  | expression OR expression"""
    
    if p[1] == "~": p[0] = ("not", p[2])
    elif p[2] == ">": p[0] = ("greater", p[1], p[3])
    elif p[2] == "<": p[0] = ("less", p[1], p[3])
    elif p[2] == "=": p[0] = ("equals", p[1], p[3])
    elif p[2] == "&": p[0] = ("and", p[1], p[3])
    elif p[2] == "|": p[0] = ("or", p[1], p[3])

def p_comment(p):
    """statement : comment"""
    pass

def p_error(p):
    if p is not None:
        print(INVALID_SYMBOL % (p.value, p.lexpos, p.lineno))

