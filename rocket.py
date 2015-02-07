# Rocket
# David Witten, Noah Kim


# Import
import fractions
from ply import lex
from ply import yacc


# Set up
namespace = {}


# Lexer
tokens = [
    "COMMENT", "NUMBER", "VARIABLE",
    
    "BACKSLASH", "QUESTION", "EXCLAMATION",
    "COLON", "SEMI", "PERIOD", "COMMA",

    "PLUS", "MINUS", "TIMES", "DIVIDE", "MODULUS", "POWER", "DOLLAR",
    "EQUALS", "GREATER", "LESS", "AND", "OR", "NOT",

    "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "LBRACE", "RBRACE",
]

def t_COMMENT(t):
    r"\#.*"
    pass

def t_NUMBER(t):
    r"([0-9]*\.[0-9]+|[0-9]+)"
    t.value = fractions.Fraction(t.value)
    return t

t_VARIABLE = r"[a-zA-Z]"

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
    print("invalid character %s" % t.value)
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

def p_expression_variable(p):
    """expression : VARIABLE"""
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
    print("error", p)

yacc.yacc()


# Main
while True:
    s = input("> ")
    if s == "quit": break
    for line in s.split(";"):
        lex.input(line)
        result = yacc.parse(lexer=lex)

