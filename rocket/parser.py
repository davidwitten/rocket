# Parser
# Rocket
# Noah Kim

# Import
from rocket.lexer import tokens

# Namespace
namespace = {}

# Errors
INVALID_VARIABLE = "Parser Error: Variable '%s' does not exist"
INVALID_SYNTAX = "Parser Error: Invalid syntax '%s'"
INCORRECT_TYPE = "Parser Error: Operator '%s' requires type %s"

# Precedence
precedence = (
    ("right", "OR"),
    ("right", "AND"),
    ("right", "EQUALS"),
    ("right", "GREATER", "LESS"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("left", "MODULUS"),
    ("right", "NEGATE", "NOT"),
    ("left", "POWER"),
)

# Parsing Definitions
def p_statements(p):
    """statements : statements statement SEMI
                  | statement SEMI
    """
    pass

def p_statement_assignment(p):
    """statement : assignment"""
    pass

def p_assignment(p):
    """assignment : VARIABLE COLON expression"""
    namespace[p[1]] = p[3]
    p[0] = p[3]

def p_statement_expression(p):
    """statement : expression"""
    p[0] = p[1]
    if p[0] is not None: print(p[0])

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_expressions(p):
    """expression : LBRACKET expressions RBRACKET"""
    p[0] = p[2]

def p_expressions(p):
    """expressions : expressions COMMA expression
                   | expression
    """
    if len(p) == 2: p[0] = [p[1]]
    else: p[0] = p[1] + [p[3]]

def p_expression_list_get(p):
    """expression : expression AT NUMBER"""
    p[0] = p[1][int(p[3])]

def p_expression_variable(p):
    """expression : VARIABLE"""
    value = namespace.get(p[1])
    if value == None: print(INVALID_VARIABLE % p[1])
    else: p[0] = namespace[p[1]]

def p_expression_parenthesis(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_unary(p):
    """expression : MINUS expression %prec NEGATE
                  | NOT expression
                  | DOLLAR expression"""
    if p[1] == "-": p[0] = -p[2]
    elif p[1] == "~": p[0] = int(not p[2])
    elif p[1] == "$":
        if type(p[2]) != list: print(INCORRECT_TYPE % ("$", "List"))
        else: p[0] = list(sorted(p[2]))

def p_expression_math(p):
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

def p_expression_comparison(p):
    """expression : expression GREATER expression
                  | expression LESS expression
                  | expression EQUALS expression
                  | expression AND expression
                  | expression OR expression
    """
    if p[2] == ">": p[0] = int(p[1] > p[3])
    elif p[2] == "<": p[0] = int(p[1] < p[3])
    elif p[2] == "=": p[0] = int(p[1] == p[3])
    elif p[2] == "&": p[0] = int(bool(p[1]) and bool(p[3]))
    elif p[2] == "|": p[0] = int(bool(p[1]) or bool(p[3]))

def p_error(p):
    if p is not None: print(INVALID_SYNTAX % p.value)
