# Rocket Lex
# Noah Kim

# Import
import fractions

# Main
precedence = (
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE"),
    ("right", "NEGATE"),
    ("left", "POWER"),
)

def p_expression(p):
    """expression : NUMBER
                  | LPAREN expression RPAREN
                  | expression POWER expression
                  | MINUS expression %prec NEGATE
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
    elif p[2] == "^": p[0] = p[1] ** p[3]

def p_error(p):
    print("error", p)
