# Rocket
# David Witten, Noah Kim

# Import
import fractions
from ply import lex
from ply import yacc

# Namespace
namespace = {}

# Fractions
def nice(fraction):
    """Get the nice value of a fraction."""
    value = fraction._numerator / fraction._denominator
    return str(int(value) if int(value) == value else value)
fractions.Fraction.__repr__ = nice
    
# Lexer
tokens = [
    "COMMENT", "NUMBER", "VARIABLE",
    "BACKSLASH", "QUESTION", "EXCLAMATION",
    "COLON", "SEMI", "PERIOD", "COMMA",
    "PLUS", "MINUS", "TIMES", "DIVIDE", "MODULUS", "POWER", "AT", "DOLLAR",
    "EQUALS", "GREATER", "LESS", "AND", "OR", "NOT",
    "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE",
]

# Errors
LEX_INVALID_CHAR = "Lexer Error: Invalid character '%s' at index %i on line %i"
PARSE_INVALID_VAR = "Parser Error: Variable '%s' does not exist."
PARSE_INVALID_SYNTAX = "Parser Error: Invalid syntax at line %i"

def t_COMMENT(t):
    r"\#.*"
    pass

def t_NUMBER(t):
    r"([0-9]*\.[0-9]+|[0-9]+)"
    t.value = fractions.Fraction(t.value)
    return t

t_VARIABLE = r"[a-zA-Z][a-zA-Z0-9]*"

t_BACKSLASH = r"\\"
t_QUESTION = r"\?"
t_EXCLAMATION = r"!"
t_COLON = r":"
t_SEMI = r";"
t_PERIOD = r"\."
t_COMMA = r","

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULUS = r"%"
t_POWER = r"\^"
t_AT = r"@"
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
    print(LEX_INVALID_CHAR % (t.value, t.lexpos, t.lineno))
    t.lexer.exitcode = 1
    t.lexer.skip(1)

t_ignore = " \t"

lex.lex()

# Parser
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
    """assignment : VARIABLE COLON expression"""
    namespace[p[1]] = p[3]
    p[0] = p[3]

def p_statement_expression(p):
    """statement : expression"""
    p[0] = p[1]

def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = p[1]

def p_expression_list(p):
    """expression : LBRACKET expressions RBRACKET"""
    p[0] = p[2]

def p_items_item(p):
    """expressions : expressions COMMA expression
                   | expression"""
    if len(p) == 2: p[0] = [p[1]]
    else: p[0] = p[1] + [p[3]]

def p_expression_list_get(p):
    """expression : expression AT NUMBER"""
    p[0] = p[1][int(p[3])]

def p_expression_variable(p):
    """expression : VARIABLE"""
    value = namespace.get(p[1])
    if value == None:
        print(PARSE_INVALID_VAR % p[1])
        return
    p[0] = namespace[p[1]]

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

def p_statement_print(p):
    """statement : BACKSLASH expression"""
    print(p[2])

def p_error(p):
    if p is not None: print(PARSE_INVALID_SYNTAX)

yacc.yacc()


# Main
while True:
    s = input("> ")
    if s == "quit": break
    for line in s.split(";"):
        lex.exitcode = 0
        lex.input(line)
        if lex.exitcode == 0:
            result = yacc.parse(lexer=lex)
            if result is not None: print(result)
        
