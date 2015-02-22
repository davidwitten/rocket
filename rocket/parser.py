# Parser
# Rocket
# Noah Kim

# Import
import fractions
from rocket.lexer import tokens

# Namespace
namespace = {}

# Errors
INVALID_SYMBOL = "Parser Error: Invalid symbol '%s' at index %i on line %i"
INVALID_VARIABLE = "Parser Error: Variable '%s' does not exist"
INVALID_OPERAND = "Parser Error: Operator '%s' requires operand%s type %s"
BAD_INDEX = "Parser Error: Index out of range of list"
INVALID_STATEMENT = "Parser Error: Error in statement at index %i on line %i"

# Precedence
precedence = (
    ("right", "OR"),
    ("right", "AND"),
    ("right", "EQUALS"),
    ("right", "GREATER", "LESS"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("left", "MODULUS"),
    ("left", "AT"),
    ("right", "NEGATE", "NOT", "DOLLAR"),
    ("left", "POWER"),
)

# Parsing Definitions
def p_statements(p):
    """statements : statements statement SEMI
                  | statement SEMI
    """
    if len(p) == 4: p[0] = p[1] + [p[2]]
    elif len(p) == 3: p[0] = [p[1]]

def p_statement_assignment(p):
    """statement : assignment"""
    p[0] = p[1]

def p_assignment(p):
    """assignment : VARIABLE COLON expression"""
    if len(p) == 4:
        namespace[p[1]] = p[3]
        p[0] = p[3]
    elif len(p) == 6:
        for x in p: print(x)

def p_assignment_error(p):
    """assignment : VARIABLE COLON error"""
    print("Parser Error: Could not set variable to %s" % p[3])

def p_statement_expression(p):
    """statement : expression"""
    p[0] = p[1]
    if p[0] == "error":
        print(INVALID_STATEMENT % (p.lexpos(1), p.lineno(1)))
    elif p[0] is not None:
        print(p[0])

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_list(p):
    """expression : LBRACKET list RBRACKET
                  | LBRACKET RBRACKET"""
    if len(p) == 4: p[0] = p[2]
    elif len(p) == 3: p[0] = []
    
def p_list(p):
    """list : list COMMA expression
            | expression"""
    if len(p) == 2: p[0] = [p[1]]
    else: p[0] = p[1] + [p[3]]

def p_expression_variable(p):
    """expression : VARIABLE"""
    value = namespace.get(p[1])
    if value == None:
        print(INVALID_VARIABLE % p[1])
        p[0] = "error"
    else:
        p[0] = namespace[p[1]]

def p_expression_list_index(p):
    """expression : expression AT expression"""
    if type(p[1]) != list or p[3] != int(p[3]):
        print(INVALID_OPERAND % ("@", "s", "List, Integer"))
        p[0] = "error"
    else:
        p[0] = p[1][int(p[3])]

def p_expression_parenthesis(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]

def p_expression_listop(p):
    """expression : DOLLAR expression"""
    if p[1] == "$":
        if type(p[2]) != list:
            print(INVALID_OPERAND % ("$", "", "List"))
        else:
            p[0] = len(p[2])

def p_expression_math(p):
    """expression : MINUS expression %prec NEGATE
                  | expression POWER expression
                  | expression MODULUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression PLUS expression
                  | expression MINUS expression
    """
    if len(p) == 3 and type(p[2]) != fractions.Fraction:
        print(INVALID_OPERAND % (p[2], "", "Number"))
        p[0] = "error"
    elif len(p) == 4 and type(p[1]) != fractions.Fraction and type(p[3]) != fractions.Fraction:
        print(INVALID_OPERAND % (p[2], "s", "Number, Number"))
        p[0] = "error"
    elif p[1] == "-": p[0] = -p[2]
    elif p[2] == "^": p[0] = p[1] ** p[3]
    elif p[2] == "%": p[0] = p[1] % p[3]
    elif p[2] == "*": p[0] = p[1] * p[3]
    elif p[2] == "/": p[0] = p[1] / p[3]
    elif p[2] == "+": p[0] = p[1] + p[3]
    elif p[2] == "-": p[0] = p[1] - p[3]

def p_expression_comparison(p):
    """expression : NOT expression
                  | expression GREATER expression
                  | expression LESS expression
                  | expression EQUALS expression
                  | expression AND expression
                  | expression OR expression
    """
    if len(p) == 2 and type(p[1]) == type(p[3]) != fractions.Fraction:
        print(INVALID_OPERAND % (p[2], "", "Number"))
        p[0] = "error"
    elif len(p) == 3 and type(p[1]) == type(p[3]) != fractions.Fraction:
        print(INVALID_OPERAND % (p[2], "s", "Number, Number"))
        p[0] = "error"
    elif p[1] == "~": p[0] = int(not p[2])
    elif p[2] == ">": p[0] = int(p[1] > p[3])
    elif p[2] == "<": p[0] = int(p[1] < p[3])
    elif p[2] == "=": p[0] = int(p[1] == p[3])
    elif p[2] == "&": p[0] = int(bool(p[1]) and bool(p[3]))
    elif p[2] == "|": p[0] = int(bool(p[1]) or bool(p[3]))

def p_error(p):
    if p is not None:
        print(INVALID_SYMBOL % (p.value, p.lexpos, p.lineno))

